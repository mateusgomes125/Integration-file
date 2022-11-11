import config.db_config as db

db_conn = db.connect_db()

data = '';cod_c = '';cod_p = '';qtd = ''

values = ''

query = """ query """

def corte(corte):
    for linha in corte:
        data = linha[2:11]
        cod_c = linha[12:18]
        cod_p = linha[19:25]
        qtd = linha[26:32]

        value = ("('" + data +"', '" + cod_c + "', '" + cod_p + "', '"  + qtd+"'),")

        values += value

        data = '';cod_c = '';cod_p = '';qtd = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)