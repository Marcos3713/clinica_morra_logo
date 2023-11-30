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
(3) Retornar ao Menu'''))
  if confirmar==1:
    buscarMedico
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
