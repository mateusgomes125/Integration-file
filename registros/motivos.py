import config.db_config as db

db_conn = db.connect_db()

cod = '';motivo = ''

values = ''

query = """ query """

def ola():
    print('')

def motivos(motivos):
    for linha in motivos:
        cod = linha[2:4]
        motivo = linha[5:34]

        value = ("('" + cod +"', '" + motivo +"'),")

        values += value

        cod = '';motivo = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
        # cursor.execute(query + values)
        # conn.commit()
    db.disconnect_db(db_conn)