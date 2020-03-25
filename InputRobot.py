import time
import mysql.connector
import keyboard
import os
from pynput.keyboard import Key, Controller
from mysql.connector import Error
from array import array
from threading import Thread

def listToString(s):
    str1 = ''
    for element in s:
        str1 += element[0] + '\n'
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

    while True:
        try:
            if keyboard.is_pressed('f7'):

                keyboard_aux = Controller()

                text_list = listToString(records)

                for char in text_list:
                    keyboard_aux.press(char)
                    keyboard_aux.release(char)
                    time.sleep(0.02)
                    if keyboard.is_pressed('f8'):
                        break
                    if keyboard.is_pressed('f6'):
                        while(keyboard.is_pressed('f7') == False):
                            pass
                break

        except KeyboardInterrupt:

            break
