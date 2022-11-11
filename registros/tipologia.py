import db_config as db

db_conn = db.connect_db()

cod_tip = '';nome_tip = ''

values = ''

query = """ query """

def tipologia(tipologia):
    for linha in tipologia:
        cod_tip = linha[2:5]
        nome_tip = linha[6:30]

        value = ("('" + cod_tip +"', '" + nome_tip +"'),")

        values += value

        cod_tip = '';nome_tip = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)