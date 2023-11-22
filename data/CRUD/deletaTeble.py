import sqlite3
import random

from sqlite3 import Error

error = Error

con = sqlite3.connect('projeto')
cursor = con.cursor()
cursor.execute("DROP TABLE User")
con.commit()