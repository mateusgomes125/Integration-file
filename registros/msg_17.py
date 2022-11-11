import db_config as db

db_conn = db.connect_db()

msg = '';assunto = ''

values = ''

query = """ query """

def mensagem(mensagem):
    for linha in mensagem:
        msg = linha[2:35]
        assunto = linha[36:65]

        value = ("('" + msg +"', '" + assunto +"'),")

        values += value

        msg = '';assunto = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)