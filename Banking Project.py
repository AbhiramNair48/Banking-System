import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'account_schema', password = 'Slimyship41$')

name = input("Enter your Username: ")
password = input("Enter your Password: ")

print(f'''\nHello {name}!
Welcome to Our Bank.\n''')

userChoice = int(input('''What would you like to do today?
                       
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Create New Account
5. Delete Account
6. Change Username or Password

Enter choice here: '''))


cursor = connection.cursor()
cursor.execute("INSERT INTO bankAccounts (UserName, Password, Balance) VALUES ('%s', '%s', %s);" % (name, password, 0))
cursor.execute("SELECT * FROM bankAccounts;")
for row in cursor:
    print(row)

connection.commit()
cursor.close()
connection.close()