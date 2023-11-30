import sqlite3
import random
from sqlite3 import Error
error = Error

def novoCliente():
  global Gerar_id
  Gerar_id=random.randint(10000,100000)
  global Inserir_cpf
  print('\n # Cadastrar um Novo Cliente! \n')
  Inserir_cpf=str(input(' Informe o CPF:'))
  
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute("SELECT * FROM User")
  linhas=cursor.fetchall()
  #Não apagar \/
  #print(*linhas,sep='\n')
  for linha in linhas:
    if Inserir_cpf==linha[2]:
      print("\n cpf já existente\n")
      novoCliente()
      
  global Inserir_nome
  Inserir_nome=str(input(' Nome do paciente: '))
  global Inserir_dataDeNascimento
  Inserir_dataDeNascimento=str(input(' Data de Nascimento(dd-mm-aaaa): '))  
  global Inserir_telefone
  Inserir_telefone=str(input(' Telefone:'))
  global Inserir_Endereço
  Inserir_Endereço=str(input(' Endereço:'))
  global Inserir_Numero
  Inserir_Numero=str(input(' Numero:'))
  global Inserir_Bairro
  Inserir_Bairro=str(input(' Bairro:'))
  global Inserir_Complemento
  Inserir_Complemento=str(input(' Complemento:'))
  global Inserir_Cidade
  Inserir_Cidade=str(input(' Cidade:'))
  global Inserir_UF
  Inserir_UF=str(input(' UF:'))
  confirmar_informações_do_cliente()

def MenudeRetorno():
  retorno=int(input(''' 
    (1) Tenta novamente
    (2) Retornar ao Menu                   
    RESPOSTA:'''))
  if retorno==1:
    novoCliente()
  elif retorno==2:
    import MenuPrincipal
  else:
    MenudeRetorno()
  
def confirmar_informações_do_cliente():
  confirmar=int(input(f'''
    Deseja confirmar as informações?
    Nome:{Inserir_nome}
    Data de Nascimento:{Inserir_dataDeNascimento}
    CPF:{Inserir_cpf}
    Telefone:{Inserir_telefone}
    Endereço:{Inserir_Endereço}, {Inserir_Numero} - {Inserir_Bairro}, {Inserir_Cidade}/{Inserir_UF}
    Complemento: {Inserir_Complemento}
    Digite (1)SIM (2)NÃO
    Resposta: '''))
  
  if confirmar==1:
    con = sqlite3.connect('projeto')
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO User (ID,Name,Birthday,CPF,Telephone,Address,AdressNumber,District,Complement,City,UF) VALUES ({Gerar_id},'{Inserir_nome}','{Inserir_dataDeNascimento}','{Inserir_cpf}','{Inserir_telefone}','{Inserir_Endereço}','{Inserir_Numero}','{Inserir_Bairro}','{Inserir_Complemento}','{Inserir_Cidade}','{Inserir_UF}')")
    con.commit()
    print('\nCliente cadastrado com sucesso!!')
    import MenuPrincipal 
  elif confirmar==2:
    print('\n   O que deseja fazer?')
    MenudeRetorno()
  else:
    print('\n   Erro!! Resposta Invalida') 
    MenudeRetorno()
    
novoCliente()


