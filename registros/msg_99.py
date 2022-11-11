import db_config as db

db_conn = db.connect_db()

msg = ''

values = ''

query = """ query """

def mensagem(mensagem):
    for linha in mensagem:
        msg = linha[2:1201]

        value = ("('" + msg +"'),")

        values += value

        msg = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)