import sqlite3
import random
from sqlite3 import Error
error = Error

def aba_cadastro_medico():
  global Gerar_id
  Gerar_id=random.randint(10000,100000)
  global Inserir_crm
  Inserir_crm=str(input('CRM:'))
  
  consulta_sql="SELECT * FROM Doctor"
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(consulta_sql)
  linhas=cursor.fetchall()
  #print(*linhas,sep='\n')
  for linha in linhas:
    if Inserir_crm==linha[2]:
      print("\nCRM já existente\n")
      aba_cadastro_medico()
      
  global Inserir_nome
  Inserir_nome=str(input('Nome do medico: '))
  global Inserir_especialidade
  Inserir_especialidade=str(input('especialidade:'))
  
def confirmar_informações_do_medico():
  confirmar=int(input(f'''\nDeseja confirmar as informações?(1)sim (2)não\n
Nome:{Inserir_nome}
CRM:{Inserir_crm}
especialidade:{Inserir_especialidade}\n
Resposta: '''))
  
  if confirmar==1:
    con = sqlite3.connect('projeto')
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO Doctor (_id,Name,CRM,Specialty) VALUES ({Gerar_id},'{Inserir_nome}','{Inserir_crm}','{Inserir_especialidade}')")
    con.commit()
    print('Medico cadastrado com sucesso!!')
  else:
    print('Comece o cadastro novamente!')  
    aba_cadastro_medico()
    
aba_cadastro_medico()
confirmar_informações_do_medico()