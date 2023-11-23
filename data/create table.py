import sqlite3

from sqlite3 import Error

error = Error

con = sqlite3.connect('projeto')
cursor = con.cursor()

cursor.execute("CREATE TABLE Servises(ID AUTO INCREMENT PRIMARY KEY,NameOfExame VARCHAR2 (100),Valor VARCHAR2 (20),Doctor_id VARCHAR2 (12),ResponsibleDoctor VARCHAR2(25))")