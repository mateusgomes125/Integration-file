import config.db_config as db

db_conn = db.connect_db()

vlr = '';comis = '';p_cont = ''

values = ''

query = """ query """

def comissao(comissao):
    for linha in comissao:
        vlr = linha[2:11]
        comis = linha[12:21]
        p_cont = linha[22:30]

        value = ("('" + vlr +"', '" + comis + "', '" + p_cont + "'),")

        values += value

        vlr = '';comis = '';p_cont = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
        # cursor.execute(query + values)
        # conn.commit()
    db.disconnect_db(db_conn)