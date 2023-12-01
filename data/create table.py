import sqlite3

from sqlite3 import Error

error = Error

con = sqlite3.connect('projeto')
cursor = con.cursor()
cursor.execute(f"UPDATE Servises SET Doctor_id = '18165' WHERE ID=56706")
con.commit()
print('exame deletado com sucesso')