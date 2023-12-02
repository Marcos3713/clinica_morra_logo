import sqlite3
from sqlite3 import Error
error = Error

def Agenda():
  print('\n\/ Agenda \/')
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(f"SELECT ExamType,_id,CPF_User,NameUser,Name_Doctor,ExamName,ExamDate,RequestDate FROM Exams WHERE result=NULL")
  global cont
  global response2
  cont=1
  response2 = cursor.fetchall()
  print("  {:<10} {:<8} {:<8} {:<10} {:<35} {:<10} {:<15} {:<10}".format("Tipo","ID","CPF", "Nome", "Médico","Exame","Data Agendada","Data da Requisição"))
  print('-'*100)
  for v in response2:
    pli,name,pla, age, perc,bla,ble,bli = v
    print(cont,"{:<10} {:<8} {:<8} {:<10} {:<35} {:<10} {:<15} {:<10}".format(pli,name,pla, age, perc,bla,ble,bli))
    cont=cont+1
  cont=int(input('Digite o numero do exame escolhido:'))
  aba_de_confirmacao()

def aba_de_confirmacao():
  confirmar=int(input(''' 
    (1) Finalizar
    (2) Deletar 
    (3) Retornar ao menu principal 
    RESPOSTA:'''))
  if confirmar==1:
    FinalizarExam()
  elif confirmar==2:
    DeletarConsuta()
  elif confirmar==3:
    import MenuPrincipal
  else:
    aba_de_confirmacao()
    
def aba_de_confirmacao2(): 
  confirmar=int(input(''' 
    (1) Voltar a Agenda
    (2) Retornar ao menu principal                   
    RESPOSTA:'''))
  if confirmar==1:
    Agenda()
  elif confirmar==2:
    import MenuPrincipal
  else:
    aba_de_confirmacao2()

def FinalizarExam():
  result=str(input('Digite o resulado: '))
  Observacao=str(input('Digite alguma Observação: '))
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  print(response2[cont-1][1])
  cursor.execute(f"UPDATE Exams SET Result = '{result}' WHERE _id={response2[cont-1][1]}")
  cursor.execute(f"UPDATE Exams SET Observation = '{Observacao}' WHERE _id={response2[cont-1][1]}")
  con.commit()
  print('Finalizado com sucesso!!!')
  aba_de_confirmacao2()

def DeletarConsuta():
  certeza=int(input('''tem certeza que deseja deletar os registros desse cliente?
  (1)sim
  (2)não
  resposta:'''))
  
  if certeza==1:
    con = sqlite3.connect('projeto')
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM Exams WHERE _id = {response2[cont-1][1]}")
    con.commit()
    print('Resgistro deletado com sucesso!!')
    aba_de_confirmacao2()
  elif certeza==2:
    aba_de_confirmacao2()
  else:
    print('resposta invalida')
    deletar_cliente()
Agenda()