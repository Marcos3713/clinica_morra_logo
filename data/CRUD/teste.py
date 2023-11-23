import sqlite3
import random
from sqlite3 import Error
error = Error


con = sqlite3.connect('projeto')
cursor = con.cursor()
cursor.execute(f"SELECT * FROM Doctor")
global response
global cont
cont=1
response = cursor.fetchall()
print(f'\nID\tNome\tCRM\tEspecialidade')
print('-'*40)
for linha in response:
  print(f'{cont}-{linha[0]}\t|{linha[1]}\t|{linha[2]}\t|{linha[3]}')
  cont=cont+1
cont=1
idDoctor=str(input('Digite o numero do medico escolhido:'))
print(response[cont-1][1])
