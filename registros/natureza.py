import db_config as db

# conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(endereco, usuario, banco, senha, sslmode)
db_conn = db.connect_db()

cod_nat = '';natureza = '';conf6 = ''
bonif =''; vlr_min = ''; bco = ''
values = ''

query = """ query """

def natureza(naturezas):
    for linha in naturezas:
        cod_nat = linha[2:4]
        natureza = linha[5:24]
        conf6 = linha[25]
        bonif = linha[26]
        vlr_min = linha[27:31]
        bco = linha[32:34]

        value = ("('" + cod_nat +"', '" + natureza + "', '" + conf6 + "', '"+
        bonif + "', '" + vlr_min + "', '" + bco + "'),")
        
        values += value
        
        cod_nat = '';natureza = '';conf6 = ''
        bonif =''; vlr_min = ''; bco = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
        # cursor.execute(query + values)
        # conn.commit()
    db.disconnect_db(db_conn)
        # conn.close()

