import mysql.connector
from mysql.connector import Error


try:
    my_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Momentum.12345',
    )

    mycursor =  my_connection.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store ")
    print(f"Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if my_connection:
        my_connection.close()




