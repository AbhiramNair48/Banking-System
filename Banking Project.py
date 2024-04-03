import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'account_schema', password = 'Slimyship41$')

sampleQuery = ('SELECT * FROM account_schema.Workers;')
addData = ('INSERT INTO Workers VALUES (9, "Abhiram", 50000, "Books");')
cursor = connection.cursor()
cursor.execute(addData)
cursor.execute(sampleQuery)
for row in cursor:
    print(row)

connection.commit()
cursor.close()
connection.close()

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