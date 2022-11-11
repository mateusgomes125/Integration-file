import config.db_config as db

db_conn = db.connect_db()

cod_cid = '';nome = ''
uf =''; cep = ''; ibge = ''

values = ''

query = """ query """

def cidade(cidade):    
    for linha in cidade:
        cod_cid = linha[2:5]
        nome = linha[6:25]
        uf = linha[26:27]
        cep = linha[28:36]
        ibge = linha[37:43]


        value = ("('" + cod_cid +"', '" + nome + "', '"+
        uf + "', '" + cep + "', '" + ibge + "'),")
        
        values += value
        
        cod_cid = '';nome = '';uf =''; cep = ''; ibge = ''

    values = values[:-1]

    db.execute_query(db_conn, query)

    db.disconnect_db(db_conn)

