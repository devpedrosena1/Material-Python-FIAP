import oracledb

with oracledb.connect(user='rm561178', password='200905', dsn='oracle.fiap.com.br/orcl') as con:
    with con.cursor() as cursor:
        status = "Incompleta"
        id = "21 or 1=1"
        upd = f"update tarefa set staus '{status}' where id={id}"
        print(upd)
        cursor.execute(upd)
    con.commit()