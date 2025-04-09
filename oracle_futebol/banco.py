import oracledb

def get_conexao():
    con = oracledb.connect(
        user="rm561178",
        password="200905",
        dsn="oracle.fiap.com.br/orcl"
    )

    return con

def entrada_valores():
    nome = input('Informe o nome do time: ')
    pontos = int(input('Informe a pontuação do time: '))

    time = {
        "nome": nome,
        "pontuacao": pontos
    }

    return time

def insere_time(time: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "insert into t_time(id, nome, pontuacao) values(gerador.nextval, :nome, :pontuacao) returning id into :id"

            new_id = cur.var(oracledb.NUMBER)
            time['id'] = new_id
            print(f'Time: {time}')
            cur.execute(sql, time)
            time['id'] = new_id.getvalue()[0]
        con.commit()
        print('Time cadastrado com sucesso!')

## def inserir_partida


if __name__ == "__main__":
    time = entrada_valores()
    insere_time(time)