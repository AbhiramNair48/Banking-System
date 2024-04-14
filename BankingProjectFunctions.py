import db_connection
import sys

connection = db_connection.get_connection()
cursor = connection.cursor()

def intro():
    global userChoice
    userChoice = int(input('''\nWhat would you like to do today?
                                                    
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Create New Account
5. Delete Account
6. Change Username or Password
7. Exit

Enter choice here: '''))
    
    return userChoice 

def getBalance(name):
    query = "SELECT Balance FROM bankAccounts WHERE UserName = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def deposit(name):
    while True:
        try:
            deposit_amount = float(input("Enter amount: "))
            if deposit_amount > 0:
                break
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    sql_query = "UPDATE bankAccounts SET Balance = Balance + %s WHERE UserName = %s"
    cursor.execute(sql_query, (deposit_amount, name))
    print(f"Successfully deposited {deposit_amount}.")
    
    connection.commit()
    
def withdraw(name):
    while True:
        try:
            withdraw_amount = float(input("Enter amount: "))
            if withdraw_amount > 0:
                break
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    sql_query = "UPDATE bankAccounts SET Balance = Balance - %s WHERE UserName = %s"
    cursor.execute(sql_query, (withdraw_amount, name))
    print(f"Successfully withdrew {withdraw_amount}.")

    
    connection.commit()
    
def createAccount():

    newAccountUser= input("Enter Account Username: ")
    newAccountPass = input("Enter Account Password: ")
    
    query = "INSERT INTO bankAccounts (UserName, Password, Balance) VALUES (%s, %s, 0)"
    cursor.execute(query, (newAccountUser, newAccountPass))
    
    connection.commit()

    
def deleteAccount(name, password):
    if input('Are you sure you want to do this?\n Type "YES" to delete account: ') == "YES":
      query = "DELETE FROM bankAccounts WHERE UserName = %s AND Password = %s"
      cursor.execute(query, (name, password))
      sys.exit("Your account has been deleted. Goodbye!")
      
    else:
        print("Ok, your account will remain active.")
      
    connection.commit()
    
def changeCredentials(name):
    
    new_username = input("Enter new username (Enter current username if you do not want to change it): ")
    new_password = input("Enter new password (Enter current password if you do not want to change it): ")

    query = "UPDATE bankAccounts SET UserName = %s WHERE UserName = %s"
    cursor.execute(query, (new_username, name))
    print(f"Successfully changed username to {new_username}.")


    query = "UPDATE bankAccounts SET Password = %s WHERE UserName = %s"
    cursor.execute(query, (new_password, name))
    print(f"Successfully changed password for {name}.")

    connection.commit()   