import config.db_config as db

db_conn = db.connect_db()

cod_atv = '';nome_atv = ''

values = ''

query = """ query """

def atividade(atividade):
    for linha in atividade:
        cod_atv = linha[2:5]
        nome_atv = linha[6:30]

        value = ("('" + cod_atv +"', '" + nome_atv +"'),")

        values += value

        cod_atv = '';nome_atv = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)