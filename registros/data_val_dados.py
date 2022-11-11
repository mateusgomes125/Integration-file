import config.db_config as db

db_conn = db.connect_db()

data = '';nr_dia = ''
gp =''; data_man = ''; nr_man = ''

values = ''

query = """ query """

def data_val_dados(data_val_dados):    
    for linha in data_val_dados:
        data = linha[2:11]
        nr_dia = linha[12:13]
        # gp = linha[14]
        # data_man = linha[15:24]
        # nr_man = linha[25:30]


        value = ("('" + data +"', '" + nr_dia + "', '"+ "'),")
        
        values += value
        
        data = '';nr_dia = '';gp =''; data_man = ''; nr_man = ''

    values = values[:-1]

    db.execute_query(db_conn, query)

    db.disconnect_db(db_conn)

