import db_config as db

db_conn = db.connect_db()

cod = '';tab = '';prc = ''

values = ''

query = """ query """

def preco(preco):
    for linha in preco:
        cod = linha[2:8]
        tab = linha[9:10]
        prc = linha[11:16]

        value = ("('" + cod +"', '" + tab + "', '" + prc + "'),")

        values += value

        cod = '';tab = '';prc = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)