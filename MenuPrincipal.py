def MenuPrincipal():
  inicio=int(input("""
    Olá, Bem-vindo a Clínica Morra Logo!
    Selecione a área que deseja acessar:
    1) Clientes
    2) Médicos
    3) Exames
    resposta: """))

  if inicio==1:
    import MenuUsuario
  elif inicio==2:
    import MenuMedicos
  elif inicio==3:
    import MenuExames
  else:
    print('\n')
    print('Resposta invalida! Tente novamente \n')
    MenuPrincipal() 
MenuPrincipal()