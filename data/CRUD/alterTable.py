import sqlite3

from sqlite3 import Error

error = Error

con = sqlite3.connect('projeto')
cursor = con.cursor()
cursor.execute("ALTER TABLE User ADD City VARCHAR(100)")