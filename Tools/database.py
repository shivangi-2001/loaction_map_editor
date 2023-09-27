import sqlite3
from sqlite3 import Error
    
def Database():
    try:
        sql = sqlite3.connect("Database.db")
        connection = sql.cursor()
        print("Database connection is started")
    except Error:
        print("Error: ", Error)
    return connection, sql

def Layout_Database(name):
    try:
        sql = sqlite3.connect(name)
        connection = sql.cursor()
        print("Layout Database connection is started")
    except Error:
        print("Error: ", Error)
    return connection, sql
