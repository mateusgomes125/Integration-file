import db_config as db

db_conn = db.connect_db()

sta = '';ped = '';dta = '';nr_nf = ''

values = ''

query = """ query """

def status_pedidos(status_pedidos):
    for linha in status_pedidos:
        sta = linha[2]
        ped = linha[3:9]
        dta = linha[4:19]
        nr_nf = linha[20:28]

        value = ("('" + sta +"', '" + ped + "', '" + dta + "', '"  + nr_nf+"'),")

        values += value

        sta = '';ped = '';dta = '';nr_nf = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
        # cursor.execute(query + values)
        # conn.commit()
    db.disconnect_db(db_conn)