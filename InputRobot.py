import time
import mysql.connector
from pynput.keyboard import Key, Controller
from mysql.connector import Error
from array import array


def listToString(s):
    str1 = ''
    for char in str(s):
        if char == '[' or char == ']' or char == ')' or char == "'" or char == ',':
            str1 += ''
        if char == '(':
            str1 += '\n'
        else:
            str1 += char
    print(str1)
    return str1


try:
    connection = mysql.connector.connect(
        host='localhost',
        database='enterprice',
        user='root',
        password=''
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        sql_select_Query = "select name from countries"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()


except mysql.connector.Error as error:
    records = "Se conecto de forma erronea"
finally:

    keyboard = Controller()

    time.sleep(2)

    text_list = listToString(str(records))

    for char in text_list:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)
