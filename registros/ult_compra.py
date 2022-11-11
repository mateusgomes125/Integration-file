import db_config as db

# conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(endereco, usuario, banco, senha, sslmode)
db_conn = db.connect_db()

cod_cli = '';p1 = '';f1 = ''
c1 =''; p2 = ''; f2 = ''
c2 = ''
values = ''

query = """ query """

def ult_compra(ult_compra):
    for linha in ult_compra:
        cod_cli = linha[2:8]
        p1 = linha[9:16]
        f1 = linha[17:24]
        c1 = linha[25:32]
        p2 = linha[33:40]
        f2 = linha[41:48]
        c2 = linha[49:56]

        value = ("('" + cod_cli +"', '" + p1 + "', '" + f1 + "', '"+
        c1 + "', '" + p2 + "', '" + f2 + "', '" + c2 + "'),")
        
        values += value
        
        cod_cli = '';p1 = '';f1 = ''
        c1 =''; p2 = ''; f2 = ''
        c2 = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
        # cursor.execute(query + values)
        # conn.commit()
    db.disconnect_db(db_conn)
        # conn.close()

