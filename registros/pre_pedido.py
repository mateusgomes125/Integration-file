import db_config as db

db_conn = db.connect_db()

cod_cli = '';cod_p = ''
qtd =''; dta = ''; vlr = ''

values = ''

query = """ query """

def pre_pedido(pre_pedido):
    
    for linha in pre_pedido:
        cod_cli = linha[2:8]
        cod_p = linha[9:15]
        qtd = linha[16:21]
        dta = linha[22:31]
        vlr = linha[32:39]


        value = ("('" + cod_cli +"', '" + cod_p + "', '"+
        qtd + "', '" + dta + "', '" + vlr + "'),")
        
        values += value
        
        cod_cli = '';cod_p = '';qtd =''; dta = ''; vlr = ''

    values = values[:-1]

    db.execute_query(db_conn, query)

    db.disconnect_db(db_conn)

