import config.db_config as db

db_conn = db.connect_db()

cam = '';qtd = '';prod = '';dsc = ''

values = ''

query = """ query """

def campanha(campanha):
    for linha in campanha:
        cam = linha[2:6]
        qtd = linha[7:12]
        prod = linha[13:19]
        dsc = linha[20:24]

        value = ("('" + cam +"', '" + qtd + "', '" + prod + "', '"  + dsc+"'),")

        values += value

        cam = '';qtd = '';prod = '';dsc = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)