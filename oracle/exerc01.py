import oracledb

def get_conexao():
    return oracledb.connect(
        user="rm561178",
        password="200905",
        dsn="oracle.fiap.com.br/orcl"
        )
print('Conexão estabelecida com sucesso!')

def entrada():
    nome = input('Informe o nome do filme: ')
    ano = int(input('Informe o ano do filme: '))

    filme = {
        'nome': nome,
        'ano': ano
    }
    return filme

def insere(dado):
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO T_FILMES(id, nome, ano) VALUES (filme_sequence.NEXTVAL, :nome, :ano)", dado)
        conn.commit()
        print('filme cadastrado com sucesso!')

if __name__ == "__main__":
    get_conexao()
    dado = entrada()
    insere(dado)