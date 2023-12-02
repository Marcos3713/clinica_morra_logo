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
    aba_de_confirmacao2()
  else:
    print('\nDados do paciente. \n')
    aba_de_confirmacao()

def aba_de_confirmacao():
  for linha in response:
    print(f'''\nID:{linha[0]}
Nome:{linha[1]}
Cpf:{linha[2]}
Data de nascimento:{linha[3]}
Telefone:{linha[4]}
Endereço:{linha[5]}, {linha[6]} - {linha[7]}, {linha[9]}/{linha[10]}
Complemento: {linha[8]}''')
  confirmar=int(input(''' 
    (1) Marcar Exame
    (2) Editar informações
    (3) Deletar cliente                  
    (4) Retornar ao menu principal
    RESPOSTA:'''))
  if confirmar==1:
    import marcarExame
  elif confirmar==2:
    editar_paciente()
  elif confirmar==3:
    deletar_cliente()
  elif confirmar==4:
    import MenuPrincipal
  else:
    aba_de_confirmacao()
    
def aba_de_confirmacao2(): 
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
    aba_de_confirmacao2()

def deletar_cliente():
  certeza=int(input('''tem certeza que deseja deletar os registros desse cliente?
  (1)sim
  (2)não
  resposta:'''))
  
  if certeza==1:
    cord=busca
    con = sqlite3.connect('projeto')
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM User WHERE cpf = {cord}")
    con.commit()
    print('Paciente deletado com sucesso')
    aba_de_confirmacao2()
  elif certeza==2:
    aba_de_confirmacao()
  else:
    print('resposta invalida')
    deletar_cliente()

def editar_paciente():
  coluna=''
  textoAlter=''  
  edit=int(input('''Qual das informações deseja editar:
        (1) Nome;
        (2) Cpf;
        (3) Data de nascimento;
        (4) Telefone;
        (5) Endereço;
        (6) Número;
        (7) Bairro;
        (8) Complemento;
        (9) Cidade;
        (10) UF;
        Resposta:'''))
  if edit==1:
    coluna='Name'
    textoAlter='o nome'
  elif edit==2:
    coluna='CPF'
    textoAlter='o cpf'
  elif edit==3:
    coluna='Birthday'
    textoAlter='a data de nascimento'
  elif edit==4:
    coluna='Telephone'
    textoAlter='o telefone'
  elif edit==5:
    coluna='Address'
    textoAlter='o endereço'
  elif edit==6:
    coluna='AdressNumber'
    textoAlter='o número do endereço'
  elif edit==7:
    coluna='District'
    textoAlter='o Bairro'
  elif edit==8:
    coluna='Complement'
    textoAlter='o complemento'
  elif edit==9:
    coluna='City'
    textoAlter='qual a cidade'
  elif edit==10:
    coluna='UF'
    textoAlter='UF'
  else:
    print('RESPOSTA INVALIDA!!!!')
    editar()  

  novoDado=str(input(f'Digite o {textoAlter}:'))
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"UPDATE  User SET {coluna} = '{novoDado}' WHERE CPF={busca}")
  con.commit()
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"SELECT * FROM User WHERE cpf = {busca}")
  global response
  response = cursor.fetchall()
  print('Usuario Alterado com sucesso!!!')
  aba_de_confirmacao()  

buscarPaciente()

    