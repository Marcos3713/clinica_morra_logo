import sqlite3
import random

from sqlite3 import Error

error = Error

class MenuMedicos():
  inicio=int(input("""        
  Área dos MEDICOS!!
  o que você deseja fazer?:
  1) Buscar um Medico
  2) Cadastrar um Medico
  3) Voltar
  resposta: """))

  if inicio==1:
    import Clientes.buscarCliente as buscarCliente
    buscarCliente
  elif inicio==2:
    import Medicos.novoMedico as novoMedico
    novoMedico
  elif inicio==3:
    import MenuPrincipal
    MenuPrincipal
  else:
    print('\nResposta invalida! Tente novamente \n') 
    MenuMedicos()
MenuMedicos()