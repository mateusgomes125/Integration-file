import db_config as db

db_conn = db.connect_db()

cod = ' '; ref = ''; descr = ''; descr_red = ''; grp = ''; sub = ''; 
div = ''; un = ''; un_v = ''; qtd_un = ''; qtd_min = ''; faixa = ''; peso = ''; 
peso_cd = ''; barra = ''; tvd = ''; flex = ''; ori_merc = ''; icm = ''; aliq_icm = ''; 
base = ''; ncm = ''; cto = ''; imposto = ''; mva = ''; aliq_st = ''; tab_pis = ''; 
aliq_pis = ''; tab_cof = ''; aliq_cof = ''; p_d = ''; cep = ''; mail = ''; emp = ''; p_fj = ''; 
cpf = ''; consu = ''; nr_estab = ''; obs2 = ''

query = ("""INSERT INTO cliente (cod, ref , descr, descr_red, grp, sub, div, un,  
un_v, qtd_un, qtd_min, faixa, peso, barra, ncm)  
VALUES """)

def produto(produto):
    for linha in produto:
        cod = linha[2:8]
        ref = linha[9:18]
        descr = linha[19:38]
        descr_red = linha[39:52]
        grp = linha[53:55]
        sub = linha[56:58]
        div = linha[59:61]
        un = linha[62:63]
        un_v = linha[64:65]
        qtd_un = linha[66:71]
        qtd_min = linha[72:75]
        faixa = linha[76:79]
        peso = linha[80:85]
        # peso_cd = linha[86:91]
        barra = linha[92:105]
        # tvd = linha[106:107]
        # flex = linha[108]
        # ori_merc = linha[109]
        # icm = linha[110:111]
        # aliq_icm = linha[112:115]
        # base = linha[116:124]
        ncm = linha[125:132]
        # cto = linha[291]
        # imposto = linha[292:311]
        # mva = linha[312:319]
        # aliq_st = linha[322:329]
        # tab_pis = linha[330:337]
        # aliq_pis = linha[346:355]
        # tab_cof =  linha[356:363]
        # aliq_cof = linha[372]
        # p_d = linha[373:384]
        # cep = linha[385:392]
        # mail = linha[394:443]
        # emp = linha[444:446]
        # p_fj = linha[447]
        # cpf = linha[448:458]
        # consu = linha[459]
        # nr_estab = linha[460:465]
        # obs2 = linha[466:699]        

        value = ("('" + cod+"', '"+ ref+"', '"+ descr+"', '"+ descr_red+"', '"+ grp+"', '"+ sub+"', '"+ div+"', '"+ 
        un+"', '"+ un_v+"', '"+ qtd_un+"', '"+ qtd_min+"', '"+ faixa +"', '"+ peso+"', '"+ barra + "', '"+ ncm+ "'),")
    
        values += value

        cod = ' '; ref = ''; descr = ''; descr_red = ''; grp = ''; sub = ''; 
        div = ''; un = ''; un_v = ''; qtd_un = ''; qtd_min = ''; faixa = ''; peso = ''; 
        peso_cd = ''; barra = ''; tvd = ''; flex = ''; ori_merc = ''; icm = ''; aliq_icm = ''; 
        base = ''; ncm = ''; cto = ''; imposto = ''; mva = ''; aliq_st = ''; tab_pis = ''; 
        aliq_pis = ''; tab_cof = ''; aliq_cof = ''; ie = ''; cep = ''; mail = ''; emp = ''; p_fj = ''; 
        cpf = ''; consu = ''; nr_estab = ''; obs2 = ''

    values = values[:-1]

    db.execute_query(db_conn, query)

    db.disconnect_db(db_conn)