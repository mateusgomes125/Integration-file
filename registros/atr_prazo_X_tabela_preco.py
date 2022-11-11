import config.db_config as db

db_conn = db.connect_db()

pzo = '';tab = '';p1 = ''
f2 =''; p2 = ''; f3 = ''
p3 = ''; f4 = ''; p4 = ''
values = ''

query = """ query """

def atr_prazo_X_tabela_preco(atr_prazo_X_tabela_preco):
    for linha in atr_prazo_X_tabela_preco:
        pzo = linha[2:4]
        tab = linha[5:6]
        p1 = linha[7:9]
        f2 = linha[10]
        p2 = linha[11:13]
        f3 = linha[14]
        p3 = linha[15:17]
        f4 = linha[18]
        p4 = linha[19:21]

        value = ("('" + pzo +"', '" + tab + "', '" + p1 + "', '"+
        f2 + "', '" + p2 + "', '" + f3 + "', '" + p3 + "', '" + f4 + "', '" + p4 +"'),")
        
        values += value
        
        pzo = ''; tab = ''; p1 = ''
        f2 =''; p2 = ''; f3 = ''
        p3 = ''; f4= ''; p4 = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
        # cursor.execute(query + values)
        # conn.commit()
    db.disconnect_db(db_conn)
        # conn.close()

