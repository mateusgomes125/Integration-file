import config.db_config as db

db_conn = db.connect_db()

grp = '';sub = '';div = '';msg_d = ''

values = ''

query = """ query """

def grupo_sub_div(grupo_sub_div):
    for linha in grupo_sub_div:
        grp = linha[2:4]
        sub = linha[5:7]
        div = linha[7:9]
        msg_d = linha[10:39]

        value = ("('" + grp +"', '" + sub + "', '" + div + "', '"  + msg_d+"'),")

        values += value

        grp = '';sub = '';div = '';msg_d = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)