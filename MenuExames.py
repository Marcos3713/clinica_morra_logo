def MenuExames():
  inicio=int(input("""        
  Área de EXAMES!!
  o que você deseja fazer?:
  1) Consultar Agenda
  2) Agendar Consulta/Exame
  3) Adicionar Serviço
  4) Buscar Serviço
  5) Voltar
  resposta: """))

  if inicio==1:
    import Consultar_agenda
  elif inicio==2:
    import marcarExame
  elif inicio==3:
    import addServiso
  elif inicio==4:
    import buscarServiso
  elif inicio==5:
    import MenuPrincipal
  else:
    print('\nResposta invalida! Tente novamente \n') 
    MenuExames()
MenuExames()