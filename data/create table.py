import sqlite3

from sqlite3 import Error

error = Error

con = sqlite3.connect('projeto')
cursor = con.cursor()
cursor.execute(f"ALTER TABLE Exams DROP COLUMN Specialty_Doctor;")
con.commit()
print('exame deletado com sucesso')