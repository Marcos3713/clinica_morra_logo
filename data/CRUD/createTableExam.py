import sqlite3

from sqlite3 import Error

error = Error

con = sqlite3.connect('projeto')
cursor = con.cursor()
cursor.execute("CREATE TABLE Exams(_id AUTO INCREMENT PRIMARY KEY, User_id VARCHAR(200), Doctor_id VARCHAR(200), ExamType VARCHAR(100), ExamDate VARCHAR(100), RequestDate VARCHAR(100), Result VARCHAR(1000), Observation VARCHAR(3000))")