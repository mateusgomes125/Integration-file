import config.db_config as db

db_conn = db.connect_db()

cod_cli = ' '; nome = ''; fant = ''; roteiro = ''; contato = ''; aniv = ''; 
end = ''; bairro = ''; cod_nat = ''; pzo = ''; sit = ''; esp = ''; cod_cid = ''; 
fone = ''; celular = ''; tab = ''; cgc = ''; cod_bco = ''; cod_tip = ''; pre_ped = ''; 
vis1 = ''; vis2 = ''; vis3 = ''; obs1 = ''; med_compra = ''; m_real = ''; m_peso = ''; 
d_ult_comp = ''; lim_c = ''; b = ''; ie = ''; cep = ''; mail = ''; emp = ''; p_fj = ''; 
cpf = ''; consu = ''; nr_estab = ''; obs2 = ''

query = ("""INSERT INTO cliente (cod_cli, nome , fant, roteiro, contato, aniv, ende, bairro,  
cod_nat, pzo, sit, esp, cod_cid, fone, celular,tab, cgc, cod_bco, cod_tip, pre_ped, vis1, vis2, vis3, obs1,  
med_compra, m_real, m_peso, d_ult_comp, lim_c, b, ie, cep, mail, emp, p_fj, cpf, consu, nr_estab, obs2)  
VALUES """)

def clientes(clientes):
    for linha in clientes:
        cod_cli = linha[2:8]
        nome = linha[9:53]
        fant = linha[54:83]
        roteiro = linha[84:87]
        contato = linha[88:112]
        aniv = linha[113:122]
        ende = linha[123:167]
        bairro = linha[168:187]
        cod_nat = linha[188:190]
        pzo = linha[191:192]
        sit = linha[193]
        esp = linha[194]
        cod_cid = linha[195:198]
        fone = linha[199:213]
        celular = linha[214:228]
        tab = linha[229:230]
        cgc = linha[231:244]
        cod_bco = linha[245:247]
        cod_tip = linha[248:251]
        pre_ped = linha[252]
        vis1 = linha[289]
        vis2 = linha[290]
        vis3 = linha[291]
        obs1 = linha[292:311]
        med_compra = linha[312:319]
        m_real = linha[322:329]
        m_peso = linha[330:337]
        d_ult_comp = linha[346:355]
        lim_c =  linha[356:363]
        b = linha[372]
        ie = linha[373:384]
        cep = linha[385:392]
        mail = linha[394:443]
        emp = linha[444:446]
        p_fj = linha[447]
        cpf = linha[448:458]
        consu = linha[459]
        nr_estab = linha[460:465]
        obs2 = linha[466:699]        

        value = ("('" + cod_cli+"', '"+ nome+"', '"+ fant+"', '"+ roteiro+"', '"+ contato+"', '"+ aniv+"', '"+ end+"', '"+ 
        bairro+"', '"+ cod_nat+"', '"+ pzo+"', '"+ sit+"', '"+ esp+"', '"+ cod_cid+"', '"+ fone+"', '"+ celular+"', '"+ tab+"', '"+ cgc+"', '"+ 
        cod_bco+"', '"+ cod_tip+"', '"+ pre_ped+"', '"+ vis1+"', '"+ vis2+"', '"+ vis3+"', '"+ obs1+"', '"+ med_compra+"', '"+ 
        m_real+"', '"+ m_peso+"', '"+ d_ult_comp+"', '"+ lim_c+"', '"+ b+"', '"+ ie+"', '"+ cep+"', '"+ mail+"', '"+ emp+"', '"+ p_fj+"', '"+ 
        cpf+"', '"+ consu+"', '"+ nr_estab+"', '"+ obs2 + "'),")
    
        values += value

        cod_cli = ' '; nome = ''; fant = ''; roteiro = ''; contato = ''; aniv = ''; 
        end = ''; bairro = ''; cod_nat = ''; pzo = ''; sit = ''; esp = ''; cod_cid = ''; 
        fone = ''; celular = ''; tab = ''; cgc = ''; cod_bco = ''; cod_tip = ''; pre_ped = ''; 
        vis1 = ''; vis2 = ''; vis3 = ''; obs1 = ''; med_compra = ''; m_real = ''; m_peso = ''; 
        d_ult_comp = ''; lim_c = ''; b = ''; ie = ''; cep = ''; mail = ''; emp = ''; p_fj = ''; 
        cpf = ''; consu = ''; nr_estab = ''; obs2 = ''

    values = values[:-1]

    db.execute_query(db_conn, query)

    db.disconnect_db(db_conn)