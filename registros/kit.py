import config.db_config as db

db_conn = db.connect_db()

desc_kit = '';cod_p = ''
descr =''; qtd = ''; prc = ''

values = ''

query = """ query """

def kit(kit):    
    for linha in kit:
        desc_kit = linha[2:11]
        cod_p = linha[12:18]
        descr = linha[19:48]
        qtd = linha[49:55]
        prc = linha[56:62]


        value = ("('" + desc_kit +"', '" + cod_p + "', '"+
        descr + "', '" + qtd + "', '" + prc + "'),")
        
        values += value
        
        desc_kit = '';cod_p = '';descr =''; qtd = ''; prc = ''

    values = values[:-1]

    db.execute_query(db_conn, query)

    db.disconnect_db(db_conn)

