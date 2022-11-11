import config.db_config as db

db_conn = db.connect_db()

cod_bco = '';bco = ''

values = ''

query = """ query """

def banco(banco):
    for linha in banco:
        cod_bco = linha[2:4]
        bco = linha[5:24]

        value = ("('" + cod_bco +"', '" + bco +"'),")

        values += value

        cod_bco = '';bco = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)