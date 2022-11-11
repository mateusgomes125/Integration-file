import config.db_config as db

db_conn = db.connect_db()

cod_grp = '';sub = ''
div =''; qtd = ''; dsc = ''

values = ''

query = """ query """
def ola():
    print('')
    
def grp(grp):  
    for linha in grp:
        cod_grp = linha[2:4]
        sub = linha[5:7]
        div = linha[8:10]
        qtd = linha[11:16]
        dsc = linha[17:21]


        value = ("('" + cod_grp +"', '" + sub + "', '"+
        div + "', '" + qtd + "', '" + dsc + "'),")
        
        values += value
        
        cod_grp = '';sub = '';div =''; qtd = ''; dsc = ''

    values = values[:-1]

    db.execute_query(db_conn, query)

    db.disconnect_db(db_conn)

