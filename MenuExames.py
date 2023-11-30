def MenuExames():
  inicio=int(input("""        
  Área de EXAMES!!
  o que você deseja fazer?:
  1) Buscar Exame
  2) Marcar Exame
  3) Adicionar Serviço
  4) Voltar
  resposta: """))

  if inicio==1:
    import buscarServiso
  elif inicio==2:
    import marcarExame
  elif inicio==3:
    import addServiso
  elif inicio==3:
    import MenuPrincipal
  else:
    print('\nResposta invalida! Tente novamente \n') 
    MenuExames()
MenuExames()