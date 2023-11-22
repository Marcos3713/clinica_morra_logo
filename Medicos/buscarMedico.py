import sqlite3
import random
from sqlite3 import Error

error = Error

def aba_de_busca():
  busca=str(input('''\/ Buscar Clientes \/
  informe o CRM:'''))
  
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"SELECT * FROM Doctor WHERE CRM = {busca}")
  response = cursor.fetchall()
  if cursor.fetchall()==None: 
    print("\nUsuário não encontrado!")
    aba_de_confirmacao2()
  else:
    print('\nDados do paciente. \n')
    aba_de_confirmacao()

def aba_de_confirmacao():
  for
  confirmar=int(input(''' 
    (1)Marcar Exame
    (2)editar informações
    (3)deletar cliente                  
    (4)Retornar ao menu principal
    RESPOSTA:'''))
  if confirmar==1:
    print('aba de marcar exame')
  elif confirmar==2:
    print("Editar informações")
  elif confirmar==3:
    print('deletar cliente')
  elif confirmar==4:
    print("retornar ao menu")
    import Menu
    Menu
  else:
    aba_de_confirmacao()
    

  

aba_de_busca()
aba_de_confirmacao() print(f'''\nID:{linha[0]}
Nome:{linha[1]}
Cpf:{linha[2]}
Data de nascimento:{linha[3]}
Telefone:{linha[4]}
Endereço:{linha[5]}''')
  confirmar=int(input(''' 
    (1)Marcar Exame
    (2)Editar Informações
    (3)Deletar Cliente                  
    (4)Retornar ao menu principal
    RESPOSTA:'''))
  if confirmar==1:
    print('aba de marcar exame')
  elif confirmar==2:
    editar()
  elif confirmar==3:
    deletar_cliente()
  elif confirmar==4:
    print("retornar ao menu")
    import MenuPrincipal
    MenuPrincipal
  else:
    aba_de_confirmacao()

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
    import Rotas.MenuUsuarios as MenuUsuarios
    MenuUsuarios
  elif certeza==2:
    aba_de_confirmacao()
  else:
    print('resposta invalida')
    deletar_cliente()

def editar():
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
        (3) Complemento;
        (4) Cidade;
        (5) UF;
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
  print('Usuario Alterado com sucesso!!!')
  aba_de_confirmacao()  

aba_de_busca()
aba_de_confirmacao() 
    