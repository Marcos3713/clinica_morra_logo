import sqlite3
from sqlite3 import Error


error = Error

def aba_de_busca():
  global busca
  busca=str(input('''\/ Buscar Medico \/
  informe o CRM:'''))
  
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"SELECT * FROM Doctor WHERE CRM = {busca}")
  global response
  response = cursor.fetchall()
  if cursor.fetchall()==[]: 
    print("\nFuncionario não encontrado!")
    aba_de_confirmacao2()
  else:
    print('\nDados do Médico. \n')
    aba_de_confirmacao()

def aba_de_confirmacao():
  for linha in response:
    print(f'''\nID:{linha[0]}
Nome:{linha[1]}
CRM:{linha[2]}
Especialidade:{linha[3]}''')
  confirmar=int(input('''
    (1)editar informações
    (2)deletar Funcionario                  
    (3)Retornar ao menu principal
    RESPOSTA:'''))
  if confirmar==1:
    editar_dados()
  elif confirmar==2:
    deletar_medico()
  elif confirmar==3:
    print('retornar ao menu')
  else:
    aba_de_confirmacao()
    

def aba_de_confirmacao2(): 
  confirmar=int(input(''' 
    (1) Tenta novamente
    (2) Cadastrar novo Medico
    (3) Retornar ao menu principal                   
    RESPOSTA:'''))
  if confirmar==1:
    aba_de_busca
  elif confirmar==2:
    import novoCliente
    novoCliente
  elif confirmar==3:
    print('retornar')
  else:
    aba_de_confirmacao2()

def deletar_medico():
  certeza=int(input('''tem certeza que deseja deletar os registros desse cliente?
  (1)sim
  (2)não
  resposta:'''))
  
  if certeza==1:
    cord=busca
    con = sqlite3.connect('projeto')
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM Doctor WHERE CRM= {cord}")
    con.commit()
    print('Paciente deletado com sucesso')
    aba_de_busca()
  elif certeza==2:
    aba_de_confirmacao()
  else:
    print('resposta invalida')
    deletar_cliente()

def editar_dados():
  coluna=''
  textoAlter=''  
  edit=int(input('''Qual das informações deseja editar:
        (1) Nome;
        (2) CRM;
        (3) Especialidade
        Resposta:'''))
  if edit==1:
    coluna='Name'
    textoAlter='o nome'
  elif edit==2:
    coluna='CRM'
    textoAlter='o CRM'
  elif edit==3:
    coluna='Specialty'
    textoAlter='a especialidade'
  else:
    print('RESPOSTA INVALIDA!!!!')
    editar()  

  novoDado=str(input(f'Digite o {textoAlter}:'))
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"UPDATE Doctor SET {coluna} = '{novoDado}' WHERE CRM={busca}")
  con.commit()
  print('Usuario Alterado com sucesso!!!')
  aba_de_confirmacao()  

aba_de_busca()

    