import sqlite3
from sqlite3 import Error
error = Error

def buscarPaciente():
  global busca
  busca=str(input('''\/ Buscar Clientes \/
  informe o CPF:'''))
  
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"SELECT * FROM User WHERE cpf = {busca}")
  global response
  response = cursor.fetchall()
  if response==[]: 
    print("\nUsuário não encontrado!")
    aba_alternativa()
  else:
    print('\nDados do paciente. \n')
    aba_de_continuacao()

def aba_de_continuacao():
  for linha in response:
    print(f'''\nID:{linha[0]}
Nome:{linha[1]}
Cpf:{linha[2]}
Data de nascimento:{linha[3]}
Telefone:{linha[4]}
''')
  confirmar=int(input('''
(1) Confirmar Cliente
(2) Tentar achar outro cliente
(3) Retornar ao Menu
Resposta:'''))
  if confirmar==1:
    escolherExame()
  elif confirmar==2:
    buscarPaciente()
  elif confirmar==3:
    import MenuPrincipal
  else:
    print('Resposta invalida!!')
    aba_de_continuacao()
    
def aba_alternativa(): 
  confirmar=int(input(''' 
    (1) Tenta novamente
    (2) Cadastrar novo cliente
    (3) Retornar ao menu principal                   
    RESPOSTA:'''))
  if confirmar==1:
    buscarPaciente()
  elif confirmar==2:
    import addCliente
  elif confirmar==3:
    import MenuPrincipal
  else:
    aba_alternativa()

def escolherExame():
  global response2
  escolherTipo=int(input('''\nQual tipo de serviço deseja fazer:
(1) Consulta
(2) Exame
Resposta: '''))
  if escolherTipo==1:
    print('\/ Buscar Serviço \/')
    con = sqlite3.connect('projeto')
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM Servises")
    cont=1
    response2 = cursor.fetchall()
    print("  {:<8} {:<15} {:<10} {:<10} {:<40} {:<10}".format("ID", "Nome", "Valor","ID Médico","Médico","Tipo"))
    print('-'*100)
    for v in response2:
      name, age, perc,bla,ble,bli = v
      print(cont,"{:<8} {:<15} {:<10} {:<10} {:<40} {:<10}".format(name, age, perc,bla,ble,bli))
      cont=cont+1
      cont=int(input('Digite o numero do exame escolhido:'))
    aba_de_confirmacao()
  elif escolherTipo==2:
    print('\/ Buscar Serviço \/')
    con = sqlite3.connect('projeto')
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM Servises")
    cont=1
    response2 = cursor.fetchall()
    print(response2)
    print("  {:<8} {:<15} {:<10} {:<10} {:<40} {:<10}".format("ID", "Nome", "Valor","ID Médico","Médico","Tipo"))
    print('-'*100)
    for g in response2:
      name, age, perc, bla, ble, bli = g
      print(cont,"{:<8} {:<15} {:<10} {:<10} {:<40} {:<10}".format(name, age, perc,bla,ble,bli))
      cont=cont+1
    cont=int(input('Digite o numero do exame escolhido:'))
  else:
    print('Resposta invalida!!')
    escolherExame()

buscarPaciente()