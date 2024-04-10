import BankingProjectFunctions
import db_connection
import sys

connection = db_connection.get_connection()
cursor = connection.cursor()

name = input("Enter your Username: ")
password = input("Enter your Password: ")

Query1 = "SELECT * FROM bankAccounts WHERE UserName = %s;"
cursor.execute(Query1, (name,))
result1 = cursor.fetchone()

Query2 = "SELECT * FROM bankAccounts WHERE Password = %s"
cursor.execute(Query2, (password,))
result2 = cursor.fetchone()

if result1 and result2:
    print(f'''\nHello {name}!
Welcome to Our Bank.''')
    global userChoice
    userChoice = BankingProjectFunctions.intro()
    
else:
    newAccount = input("That account does not exist. Would you like to create a new account with us (Yes/No)? ")
    if newAccount == 'Yes':
        BankingProjectFunctions.createAccount()
    elif newAccount == 'No':
        sys.exit("Thank you for using This Bank. Hope you come again!")
    else:
        sys.exit('That is not a valid choice.')

if userChoice == 0:
    
    if name == "AdminUser" and password == "AdminPass":
        adminChoice = input("You are an admin. Would you like to see the data (Yes/No)? ")
        if adminChoice == "Yes":
            query = "SELECT * FROM account_schema.bankAccounts;"
            cursor.execute(query)
            for row in cursor:
                print(row)
        else:
            print("OK")
            BankingProjectFunctions.intro()
    else:
        print("You are not an admin.")
        BankingProjectFunctions.intro()

elif userChoice == 1:
    print(f'Your account balance is currently: {BankingProjectFunctions.getBalance(name)}')
    BankingProjectFunctions.intro()

elif userChoice == 4:
    BankingProjectFunctions.createAccount()
    BankingProjectFunctions.intro()
    
elif userChoice == 5:
    BankingProjectFunctions.deleteAccount(name, password)
    BankingProjectFunctions.intro()
    
elif userChoice == 7:
    sys.exit("Thank you for using Our Bank. Come again soon!")


connection.commit()
cursor.close()
connection.close()