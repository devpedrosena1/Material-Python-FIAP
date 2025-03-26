import oracledb

con = oracledb.connect(
    user='rm561178',
    password='200905',
    dsn='oracle.fiap.com.br/orcl'
)

# update
upd = 'update T_FIAP_ALUNO set nome=:novo_nome where rm=:rm'

cursor = con.cursor()

dado = {
    'novo_nome': 'Matteus Viegas',
    'rm': 561090
}

cursor.execute(upd, dado)
con.commit()
print('Aluno atualizado com sucesso!')

cursor.close()
con.close()