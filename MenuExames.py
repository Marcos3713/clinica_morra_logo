class MenuExames():
  inicio=int(input("""        
  Área de EXAMES!!
  o que você deseja fazer?:
  1) Buscar Exame
  2) Marcar Exame
  3) Voltar
  resposta: """))

  if inicio==1:
    import Clientes.buscarCliente as buscarCliente
  elif inicio==2:
    import Clientes.novoCliente as novoCliente
  elif inicio==3:
    import MenuPrincipal
  else:
    print('\nResposta invalida! Tente novamente \n') 
    MenuExames()
MenuExames()