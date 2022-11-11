import config.db_config as db

# conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(endereco, usuario, banco, senha, sslmode)
db_conn = db.connect_db()

cod_p = '';qtd = '';dta_f = ''
s =''; dias = ''; dta_val = ''
values = ''

query = """ query """

def gravosos(gravosos):
    for linha in gravosos:
        cod_p = linha[2:8]
        qtd = linha[9:17]
        dta_f = linha[18:27]
        s = linha[28]
        dias = linha[29:33]
        dta_val = linha[34:43]

        value = ("('" + cod_p +"', '" + qtd + "', '" + dta_f + "', '"+
        s + "', '" + dias + "', '" + dta_val + "'),")
        
        values += value
        
        cod_p = '';qtd = '';dta_f = ''
        s =''; dias = ''; dta_val = ''


    values = values[:-1]

    db.execute_query(db_conn, query)
        # cursor.execute(query + values)
        # conn.commit()
    db.disconnect_db(db_conn)
        # conn.close()

