import sqlite3
import random

from sqlite3 import Error

error = Error

def MenuUsuarios():
  inicio=int(input("""        
  Área de CLIENTES!!
  o que você deseja fazer?:
  1) Buscar um cliente
  2) Cadastrar um cliente
  3) Marcar Exame
  4) Marcar consulta
  5) Voltar
  resposta: """))

  if inicio==1:
    import Clientes.buscarCliente as buscarCliente
    buscarCliente
  elif inicio==2:
    import Clientes.novoCliente as novoCliente
    novoCliente
  elif inicio==3:
    MenuUsuarios()
  elif inicio==4:
    MenuUsuarios()
  elif inicio==5:
    import MenuPrincipal
    MenuPrincipal
  else:
    print('\nResposta invalida! Tente novamente \n') 
    MenuUsuarios()
MenuUsuarios()