def MenuUsuario():
  inicio=int(input("""        
  Área de CLIENTES!!
  o que você deseja fazer?:
  1) Buscar Cliente
  2) Cadastrar Cliente
  3) Voltar
  resposta: """))

  if inicio==1:
    import buscarCliente
  elif inicio==2:
    import addCliente
  elif inicio==3:
    import MenuPrincipal
  else:
    print('\nResposta invalida! Tente novamente \n') 
    MenuUsuario()
MenuUsuario()