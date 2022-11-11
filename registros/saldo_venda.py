import db_config as db

db_conn = db.connect_db()

saldo = '';atu = ''

values = ''

query = """ query """

def saldo_venda(saldo_venda):
    for linha in saldo_venda:
        saldo = linha[2:8]
        atu = linha[9]

        value = ("('" + saldo +"', '" + atu +"'),")

        values += value

        saldo = '';atu = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
        # cursor.execute(query + values)
        # conn.commit()
    db.disconnect_db(db_conn)