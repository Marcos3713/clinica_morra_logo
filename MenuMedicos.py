def MenuMedicos():
  inicio=int(input("""        
  Área dos MÉDICOS!!
  o que você deseja fazer?:
  1) Buscar Médico
  2) Cadastrar Médico
  3) Voltar
  resposta: """))

  if inicio==1:
    import buscarMedico
  elif inicio==2:
    import addMedico
  elif inicio==3:
    import MenuPrincipal
  else:
    print('\nResposta invalida! Tente novamente \n') 
    MenuMedicos()
MenuMedicos()