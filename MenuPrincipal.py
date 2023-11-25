import sqlite3
import random
from sqlite3 import Error
error = Error


def main():
  #Pagina inicial do programa para direcionar a pessoa que acessa
  inicio=int(input("""
    Olá, Bem-vindo a Clínica Morra Logo!
    Selecione a área que deseja acessar:
    1) Clientes
    2) Médicos
    3) Exames
    resposta: """))

  if inicio==1:
    import MenuUsuarios
    main()
  elif inicio==2:
    import MenuMedicos
    main()
  elif inicio==3:
    print('aba exames')
    main()
  else:
    print('\n')
    print('Resposta invalida! Tente novamente \n')
    main() 
main()