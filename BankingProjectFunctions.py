import db_connection

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

def createAccount():

    newAccountUser= input("Enter Account Username: ")
    newAccountPass = input("Enter Account Password: ")
    
    query = "INSERT INTO bankAccounts (UserName, Password, Balance) VALUES (%s, %s, 0)"
    cursor.execute(query, (newAccountUser, newAccountPass))
    
    connection.commit()
    cursor.close()
    connection.close()
    
def deleteAccount(name, password):
    if input('Are you sure you want to do this?\n Type "YES" to delete account: ') == "YES":
      query = "DELETE FROM bankAccounts WHERE UserName = %s AND Password = %s"
      cursor.execute(query, (name, password))
      
    connection.commit()
    cursor.close()
    connection.close()
