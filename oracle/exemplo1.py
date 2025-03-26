import oracledb

conexao = oracledb.connect(
    user='rm561178', 
    password='200905', 
    dsn='oracle.fiap.com.br/orcl')

print(f"Oracle conexão {conexao.version}")

cursor = conexao.cursor()

sql = "Select * from T_FIAP_ALUNO"
cursor.execute(sql)
# Qual é o tipo de objeto Cursor?
# Cursor -> é um oracledb.Cursor

for registro in cursor:
    # registro é uma tupla (tuple)
    print(registro)

sql = "SELECT * FROM T_FIAP_ALUNO"
cursor.execute(sql)
registros = cursor.fetchall()

print(registros)

for reg in registros:
    print(reg)

cursor.close()
conexao.close()