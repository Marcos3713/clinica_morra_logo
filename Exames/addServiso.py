import sqlite3
import random
from sqlite3 import Error
error = Error

class cadastrarMedico():
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
  print("  {:<8} {:<15} {:<10} {:<10}".format("ID", "Nome", "CRM","Especialidade"))
  print('-'*70)
  for v in response:
    name, age, perc,bla = v
    print(cont,"{:<8} {:<15} {:<10} {:<10}".format(name, age, perc,bla))
    cont=cont+1
  cont=int(input('Digite o numero do medico escolhido:'))
  
  
class confirmar_informações_do_medico():
  confirmar=int(input(f'''\nDeseja confirmar as informações?(1)sim (2)não\n
Nome: {Inserir_nome}
valor: {Inserir_valor}.00
Medico resposavel: Dr(a).{response[cont-1][1]} - {response[cont-1][3]} \n
Resposta: '''))
  
  if confirmar==1:
    con = sqlite3.connect('projeto')
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO Servises (ID,NameOfExame,Valor,Doctor_id,ResponsibleDoctor) VALUES ({Gerar_id},'{Inserir_nome}','{Inserir_valor}.00','{response[cont-1][0]}','Dr(a).{response[cont-1][1]} - {response[cont-1][3]}')")
    con.commit()
    print('cadastrado finalizado com sucesso!!')
  else:
    print('Comece o cadastro novamente!')  
    cadastrarMedico()
    
cadastrarMedico()
confirmar_informações_do_medico()