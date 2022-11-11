import config.db_config as db

db_conn = db.connect_db()

razao = ' '; end = ''; nr = ''; bairro = ''; cep = ''; cod_mun = ''; 
fone = '';cgc= ''; ie = ''; mail = ''; cnae = ''; ime_tri = ''; cod_sn = ''; 
p_sn = ''

query = ("""INSERT INTO cliente (razao, end , nr , bairro, cep, cod_mun, fone ,cgc,  
ie, mail, cnae, ime_tri, cod_sn, p_sn)  
VALUES """)

def empresa(empresa):
    for linha in empresa:
        razao = linha[2:41]
        end = linha[42:71]
        nr = linha[72:75]
        bairro = linha[76:95]
        cep = linha[96:104]
        cod_mun = linha[105:108]
        fone = linha[109:118]
        cgc= linha[119:136]
        ie = linha[137:151]
        mail = linha[152:201]
        cnae = linha[202:208]
        ime_tri = linha[209]
        cod_sn = linha[210:212]
        p_sn = linha[213:217]
     

        value = ("('" + razao+"', '"+ end+"', '"+ nr +"', '"+ bairro+"', '"+ cep+"', '"+ cod_mun+"', '"+ fone +"', '"+ 
        cgc+"', '"+ ie+"', '"+ mail+"', '"+ cnae+"', '"+ ime_tri +"', '"+ cod_sn+"', '"+ p_sn + "'),")
    
        values += value

        razao = ' '; end = ''; nr = ''; bairro = ''; cep = ''; cod_mun = ''; 
        fone = '';cgc= ''; ie = ''; mail = ''; cnae = ''; ime_tri = ''; cod_sn = ''; 
        p_sn = ''

    values = values[:-1]

    db.execute_query(db_conn, query)

    db.disconnect_db(db_conn)