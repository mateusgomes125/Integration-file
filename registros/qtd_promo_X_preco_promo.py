import db_config as db

db_conn = db.connect_db()

cod_p = '';qtd = '';prc = ''

values = ''

query = """ query """

def qtd_promo_X_preco_promo(qtd_promo_X_preco_promo):
    for linha in qtd_promo_X_preco_promo:
        cod_p = linha[2:8]
        qtd = linha[9:15]
        prc = linha[16:23]

        value = ("('" + cod_p +"', '" + qtd + "', '" + prc + "'),")

        values += value

        cod_p = '';qtd = '';prc = ''

    values = values[:-1]

    db.execute_query(db_conn, query)
    db.disconnect_db(db_conn)