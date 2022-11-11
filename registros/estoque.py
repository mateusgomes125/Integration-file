import config.db_config as db

db_conn = db.connect_db()

cod = '';sinal = '';est_atu = '';emp = ''

values = ''

query = """ query """

def estoque(estoque):
    for linha in estoque:
        cod = linha[2:8]
        sinal = linha[9]
        est_atu = linha[10:21]
        emp = linha[22:24]

        value = ("('" + cod +"', '" + sinal + "', '" + est_atu + "', '"  + emp+"'),")

        values += value

        cod = '';sinal = '';est_atu = '';emp = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)