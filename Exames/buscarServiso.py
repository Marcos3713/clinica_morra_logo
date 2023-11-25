import sqlite3
from sqlite3 import Error



error = Error

def aba_de_busca():
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"SELECT * FROM Servises")
  global response
  global cont
  cont=1
  response = cursor.fetchall() 
  print("  {:<8} {:<30} {:<10} {:<10} {:<10}".format("ID", "Exame", "Valor","Medico","Especialidade"))
  print('-'*100)
  for v in response:
    id_, nameexame, valor,nameDoctor , responsable= v
    print(cont,"{:<8} {:<30} {:<10} {:<10} {:<10}".format(id_, nameexame, valor,nameDoctor , responsable))
    cont=cont+1
  cont=int(input('Digite o numero do serviço:'))
  
  
def aba_de_confirmacao():
  for linha in response:
    print(f'''\nDeseja confirmar as informações?(1)sim (2)não\n
Nome: {response[cont-1][1]}
valor: {response[cont-1][2]}
Medico resposavel: Dr(a).{response[cont-1][3]} - {response[cont-1][4]} \n
Resposta: ''')
  confirmar=int(input(''' 
    (1) editar informações
    (2) deletar Exame                 
    (3) Retornar ao menu principal
    RESPOSTA:'''))
  if confirmar==1:
    editar_exame()
  elif confirmar==2:
    deletar_exame()
  elif confirmar==3:
    print('Retornar ao menu')
  else:
    aba_de_confirmacao()
    

def deletar_exame():
  certeza=int(input('''tem certeza que deseja deletar esse exame?
  (1)sim
  (2)não
  resposta:'''))
  
  if certeza==1:
    con = sqlite3.connect('projeto')
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM Servises WHERE ID = {response[cont-1][0]} ")
    con.commit()
    print('exame deletado com sucesso')
  elif certeza==2:
    aba_de_confirmacao()
  else:
    print('resposta invalida')
    deletar_exame()

def editar_exame():
  global coluna
  coluna =''
  global coluna2
  coluna2 =''
  global textoAlter
  textoAlter=''
  global floate
  floate='' 
  edit=int(input('''\nQual das informações deseja editar:
  (1) Nome;
  (2) Valor;
  (3) Medico Resposavel;
  Resposta:'''))
  if edit==1:
    coluna='NameOfExame'
    textoAlter='o nome'
    update1()
  elif edit==2:
    coluna='Valor'
    textoAlter='o valor'
    floate='.00'
    update1()
  elif edit==3:
    coluna='Doctor_id'
    coluna2='ResponsibleDoctor'
    update2()
  else:
    print('RESPOSTA INVALIDA!!!!')
    editar_exame()  

  print('\n\tExame Alterado com sucesso!!!')
  aba_de_confirmacao() 
def update1():
  novoDado=str(input(f'Digite o {textoAlter}:'))
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"UPDATE Servises SET {coluna} = '{novoDado}{floate}' WHERE ID={response[cont-1][0]}")
  con.commit()
  
def update2():
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"SELECT * FROM Doctor")
  global response2
  cont=1
  response2 = cursor.fetchall()
  print("  {:<8} {:<15} {:<10} {:<10}".format("ID", "Nome", "CRM","Especialidade"))
  print('-'*100)
  for v in response2:
    name, age, perc,bla = v
    print(cont,"{:<8} {:<15} {:<10} {:<10}".format(name, age, perc,bla))
    cont=cont+1
  cont=int(input('Digite o numero do medico escolhido:'))
  novoDado=response2[cont-1][0]
  novoDado2=f"Dr(a).{response2[cont-1][1]} - {response2[cont-1][3]}"
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"UPDATE Servises SET {coluna} = '{novoDado}' WHERE ID={response[cont-1][0]}")
  cursor.execute(f"UPDATE Servises SET {coluna2} = '{novoDado2}' WHERE ID={response[cont-1][0]}")
  con.commit()

aba_de_busca()
aba_de_confirmacao()

    