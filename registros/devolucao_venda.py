import config.db_config as db

# conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(endereco, usuario, banco, senha, sslmode)
db_conn = db.connect_db()

cod_cli = '';nf = '';cod_p = ''
qtd =''; vlr = ''; dta_dev = ''
motivo = ''
values = ''

query = """ query """

def devolucaoVenda(devolucao_vendas):
    for linha in devolucao_vendas:
        cod_cli = linha[2:8]
        nf = linha[9:17]
        cod_p = linha[18:24]
        qtd = linha[25:32]
        vlr = linha[33:40]
        dta_dev = linha[41:50]
        motivo = linha[51:80]

        value = ("('" + cod_cli +"', '" + nf + "', '" + cod_p + "', '"+
        qtd + "', '" + vlr + "', '" + dta_dev + "', '" + motivo + "'),")
        
        values += value
        
        cod_cli = '';nf = '';cod_p = ''
        qtd =''; vlr = ''; dta_dev = ''
        motivo = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
        # cursor.execute(query + values)
        # conn.commit()
    db.disconnect_db(db_conn)
        # conn.close()

