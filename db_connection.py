#Used to easily import SQL server connection to other files.
import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        user='root',
        database='account_schema',
        password='Slimyship41$'        
    )
    return connection