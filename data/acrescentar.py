import sqlite3
import random

from sqlite3 import Error

error = Error

con = sqlite3.connect('projeto')
cursor = con.cursor()
cursor.execute(f"ALTER TABLE Exams ADD ExamName VARVHAR (50)")
con.commit()