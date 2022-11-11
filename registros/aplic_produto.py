import config.db_config as db

db_conn = db.connect_db()

codigo = '';aplic = ''

values = ''

# INSERTorUPDATE_query = """INSERT INTO aplicacao_produto (codigo,aplic) VALUES"""

def aplic_produto(aplic_produto):
    for linha in aplic_produto:
        codigo = linha[2:8]
        aplic = linha[9:1057]

        value = ("('" + codigo +"', '" + aplic +"'),")

        values += value

        codigo = '';aplic = ''

    values = values[:-1]

# INSERTorUPDATE_query += values + " ON CONFLICT (codigo, aplic) DO UPDATE;"
# res = db.execute_query(db_conn, INSERTorUPDATE_query)