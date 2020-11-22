import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def vvod():
    cursor = connection.cursor()
    name = input("Name: ")
    phone = input("Phone: ")
    city = input("City: ")
    cursor.execute("""
    INSERT INTO
    `phonebook` (`name`, `phone`, `city`)
    VALUES
    (%s, %s, %s);
    """,(name, phone, city))
    connection.commit()


def display():
    df = pd.read_sql("SELECT * FROM phonebook", connection)
    print(df)

def delete():
    cur = connection.cursor()
    name = input("Name for delete: ")
    cur.execute("DELETE FROM `phonebook` WHERE `phonebook`.`name` = %s", (name,))
    connection.commit()

def search():
    cursor = connection.cursor()
    name = input()
    cursor.execute('SELECT * FROM `phonebook`')
    results = cursor.fetchall()
    for key in results:
        if key[2] == name:
            print(key[1])

def update():
    cursor = connection.cursor()
    Name = input("Enter the name: ")
    Phone = input("Enter the phone: ")
    City = input("Enter the city: ")
    Id = int(input("Enter the ID: "))
    cursor.execute("""
    UPDATE Phonebook
    SET Phone=%s, Name=%s, City=%s
    WHERE ID_Phone=%s;
    """, (Phone, Name, City, Id))
    connection.commit()



connection = create_connection("localhost", "Nik", "Nikita2002","phone_book")
update()
display()
connection.close()