import oracledb

conexao = oracledb.connect(
    user='rm561178',
    password='200905',
    dsn='oracle.fiap.com.br/orcl'
)

## insert
ins = '''Insert Into T_FIAP_ALUNO(rm, nome, turma, nota) values(:rm, :nome, :turma, :nota)'''

aluno = {
    'rm': 561090,
    'nome': 'Matteus',
    'turma': '1TDSQ',
    'nota': 8.0
}

cursor = conexao.cursor()
cursor.execute(ins, aluno)
conexao.commit()
print('Aluno inserido com sucesso!')

cursor.close()
conexao.close()