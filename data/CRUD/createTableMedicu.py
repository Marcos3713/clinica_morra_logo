import sqlite3

from sqlite3 import Error

error = Error

con = sqlite3.connect('projeto')
cursor = con.cursor()
cursor.execute("CREATE TABLE Doctor(_id AUTO INCREMENT PRIMARY KEY, Name VARCHAR(200), CRM VARCHAR(200), Specialty VARCHAR(100))")