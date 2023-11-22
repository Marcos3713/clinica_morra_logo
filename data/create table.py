import sqlite3

from sqlite3 import Error

error = Error

con = sqlite3.connect('projeto')
cursor = con.cursor()

cursor.execute("CREATE TABLE User(ID AUTO INCREMENT PRIMARY KEY,Name VARCHAR2 (100),CPF VARCHAR2 (20),Birthday VARCHAR2 (12),Telephone VARCHAR2(25),Address VARCHAR2(150),AdressNumber NUMBER(25),District VARCHAR2 (100),Complement VARCHAR (100),City VARCHAR (100),UF VARCHAR (10))")