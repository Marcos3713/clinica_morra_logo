import sqlite3
import random
from sqlite3 import Error
error = Error

def aba_cadastro_medico():
  global Gerar_id
  Gerar_id=random.randint(10000,100000)    
  global Inserir_nome
  Inserir_nome=str(input('Nome do Exame: '))
  global Inserir_valor
  Inserir_valor=str(input('valor do exame:'))
  global escolher_doctor
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
  cont=int(input('Digite o numero do medico escolhido:'))
  print(response[cont-1][1])
  
def confirmar_informações_do_medico():
  confirmar=int(input(f'''\nDeseja confirmar as informações?(1)sim (2)não\n
Nome:{Inserir_nome}
valor:{Inserir_valor}.00
Medico resposavel:Dr(a).{response[cont-1][1]}-{response[cont-1][3]} \n
Resposta: '''))
  
  if confirmar==1:
    con = sqlite3.connect('projeto')
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO Servises (ID,NameOfExame,Valor,Doctor_id,ResponsibleDoctor) VALUES ({Gerar_id},'{Inserir_nome}','{Inserir_valor}.00','{response[cont-1][1]}','{response[cont-1][3]}')")
    con.commit()
    print('cadastrado finalizado com sucesso!!')
  else:
    print('Comece o cadastro novamente!')  
    aba_cadastro_medico()
    
aba_cadastro_medico()
confirmar_informações_do_medico()