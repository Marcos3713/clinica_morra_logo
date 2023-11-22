import random

con = sqlite3.connect('projeto')
cursor = con.cursor()
cursor.execute(f"INSERT INTO teste (ID,Nome,Data_de_nascimento,exame,Medico,cpf,Telefone,Endereço,Bairro,Cidade) VALUES ({Gerar_id},'bola','23-05-2001','87991035314')")
con.commit()
  
   #ALTER TABLE nome_tabela DROP COLUMN nome_coluna
   
   #TRUNCATE TABLE
   
#ALTER TABLE paciente ADD Data_Nascimento varchar(15)

#from file import function
try:
  consulta_sql="SELECT * FROM paciente"
  con = sqlite3.connect('projeto')
  cursor = con.cursor()
  cursor.execute(consulta_sql)
  linhas=cursor.fetchall()
  print("Numero total de registros",cursor.rowcount)

  print("\nmostrando registros")
  for i in linhas:
    print("Id:",i[0],"nome:",i[1],"cpf:",i[4])
    print("\n")
except Error as e:
  print("Erro",e)
