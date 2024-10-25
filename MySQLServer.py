import pymysql
from pymysql import Error


try:
    my_connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Momentum.12345',
    )

    mycursor =  my_connection.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store ")
    print(f"Database 'alx_book_store' created successfully!")
except pymysql.Error as e:
    print(f"Error: {e}")

finally:
    if my_connection:
        my_connection.close()




