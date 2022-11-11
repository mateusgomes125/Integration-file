# import psycopg2
from ftplib import FTP_TLS, all_errors
import os
import re
import time
import ftp_con
import aplic_produto, atividade, atr_prazo_X_tabela_preco, banco, campanha
import cidade, clientes, comissao, corte, data_val_dados, devolucao_venda
import empresa, estoque, gravosos, grupo_sub_div, kit, motivos, msg_17
import msg_99, natureza, pre_pedido, preco, produto, qtd_promo_X_preco_promo
import saldo_venda, status_pedidos, tipologia, ult_compra, grupo

def changeExtension(pathf, filename):
    novaExtensao = ".txt"
    nome_sep = filename.split('.')
    nome_sep[1] = '.*' + nome_sep[1]
    # Muda extensao
    reg = re.compile(nome_sep[1])
    if os.path.isdir(pathf) and not os.path.islink(pathf):
        arquivos = os.listdir(pathf)
        for arquivo in arquivos:
            if(arquivo == filename):
                c = os.path.splitext(arquivo)
                b = c[0] + novaExtensao
                a = os.path.join(pathf,arquivo)
                b = os.path.join(pathf,b)
                os.rename(a,b)

# class Timer(threading.Thread):
#     def __init__(self, segundos):
#         self.runTime = segundos

def main():
   while True:
        file = ftp_con.ftp_connect()
        if(file):
            processfile(file)
        time.sleep(3600)

# nome = os.path.basename("/home/veplex05/integration-file/PW0014.638")
# path = "/home/veplex05/integration-file/"
# changeExtension(path, nome)

# arquivos = os.listdir(path)
# for arquivo in arquivos:
#     print(arquivo)

def processfile(file):

    dev_venda = []
    comissao = []
    motivos = []
    pre_pedido = []
    clientes = []
    saldo_venda = []
    cidade = []
    tipologia = []
    atividade = []
    atr_prazo_X_tab_preco = []
    banco = []
    natureza = []
    ult_compra = []
    status_pedidos = []
    data_val_dados = []
    produto = []
    estoque = []
    corte = []
    preco = []
    qtd_promo_X_preco_promo = []
    gravosos = []
    msg = []
    msg_geral = []
    grupo_sub_div = []
    kit = []
    grp = []
    campanha = []
    aplic_produto = []
    empresa = []
    total_linha = []

    try:
        arq = open(file, 'r', encoding='iso8859-1')
            
        texto = arq.readlines()

        for linha in texto:
            if(linha[:2] == '00'):
                dev_venda.append(linha)
                
            elif(linha[:2] == '01'):
                comissao.append(linha)

            elif(linha[:2] == '02'):
                motivos.append(linha)

            elif(linha[:2] == '03'):
                pre_pedido.append(linha)
                
            elif(linha[:2] == '05'):
                clientes.append(linha)
                
            elif(linha[:2] == '06'):
                saldo_venda.append(linha)
                
            elif(linha[:2] == '09'):
                cidade.append(linha)
                
            elif(linha[:2] == '10'):
                tipologia.append(linha)
                
            elif(linha[:2] == '27'):
                atividade.append(linha)
                
            elif(linha[:2] == '28'):
                atr_prazo_X_tab_preco.append(linha)
                
            elif(linha[:2] == '18'):
                banco.append(linha)
                
            elif(linha[:2] == '20'):
                natureza.append(linha)
                
            elif(linha[:2] == '23'):
                ult_compra.append(linha)
                
            elif(linha[:2] == '45'):
                status_pedidos.append(linha)
                
            elif(linha[:2] == '12'):
                data_val_dados.append(linha)
                
            elif(linha[:2] == '13'):
                produto.append(linha)
                
            elif(linha[:2] == '43'):
                estoque.append(linha)
                
            elif(linha[:2] == '44'):
                corte.append(linha)
                
            elif(linha[:2] == '33'):
                preco.append(linha)
                
            elif(linha[:2] == '15'):
                qtd_promo_X_preco_promo.append(linha)
                
            elif(linha[:2] == '16'):
                gravosos.append(linha)
                
            elif(linha[:2] == '17'):
                msg.append(linha)
                
            elif(linha[:2] == '99'):
                msg_geral.append(linha)
                
            elif(linha[:2] == '19'):
                grupo_sub_div.append(linha)
                
            elif(linha[:2] == '22'):
                kit.append(linha)
                
            elif(linha[:2] == '46'):
                grp.append(linha)
                
            elif(linha[:2] == '47'):
                campanha.append(linha)
                
            elif(linha[:2] == '48'):
                aplic_produto.append(linha)
                
            elif(linha[:2] == '49'):
                empresa.append(linha)
                
            elif(linha[:2] == '80'):
                total_linha.append(linha)
                
        arq.close()   

        executeregister(
            dev_venda, comissao, motivos, pre_pedido, clientes, saldo_venda, 
            cidade, tipologia, atividade, atr_prazo_X_tab_preco,
            banco, natureza, ult_compra, status_pedidos, data_val_dados,
            produto, estoque, corte, preco, qtd_promo_X_preco_promo,
            gravosos, msg, msg_geral, grupo_sub_div, kit, grp, campanha,
            aplic_produto, empresa)
        
    except:
        print('erro ao ler o arquivo')

def executeregister(
        dev_venda, comis, motiv, pre_ped, cli, saldo_v, 
        cid, tip, ativ, atr_prazo_X_tab_prec,
        bco, nature, ult_comp, status_ped, data_val_dad,
        prod, estoq, cort, prec, qtd_promo_X_preco_prom,
        gravoso, msg, msg_geral, grp_sub_div, kt, grup, campanh,
        aplic_prod, empre
):
    if(dev_venda.__sizeof__() > 0):
        devolucao_venda.devolucaoVenda()
    if(comis.__sizeof__() > 0):
        comissao.comissao()
    if(motiv.__sizeof__() > 0):
        motivos.motivos()
    if(pre_ped.__sizeof__() > 0):
        pre_pedido.pre_pedido()
    if(cli.__sizeof__() > 0):
        clientes.clientes()
    if(saldo_v.__sizeof__() > 0):
        saldo_venda.saldo_venda()
    if(cid.__sizeof__() > 0):
        cidade.cidade()
    if(tip.__sizeof__() > 0):
        tipologia.tipologia()
    if(ativ.__sizeof__() > 0):
        atividade.atividade()
    if(atr_prazo_X_tab_prec.__sizeof__() > 0):
        atr_prazo_X_tabela_preco.atr_prazo_X_tabela_preco()
    if(bco.__sizeof__() > 0):
        banco.banco()
    if(nature.__sizeof__() > 0):
        natureza.natureza()
    if(ult_comp.__sizeof__() > 0):
        ult_compra.ult_compra()
    if(status_ped.__sizeof__() > 0):
        status_pedidos.status_pedidos()
    if(data_val_dad.__sizeof__() > 0):
        data_val_dados.data_val_dados()
    if(prod.__sizeof__() > 0):
        produto.produto()
    if(estoq.__sizeof__() > 0):
        estoque.estoque()
    if(cort.__sizeof__() > 0):
        corte.corte()
    if(prec.__sizeof__() > 0):
        preco.preco()
    if(qtd_promo_X_preco_prom.__sizeof__() > 0):
        qtd_promo_X_preco_promo.qtd_promo_X_preco_promo()
    if(gravoso.__sizeof__() > 0):
        gravosos.gravosos()
    if(msg.__sizeof__() > 0):
        msg_17.mensagem()
    if(msg_geral.__sizeof__() > 0):
        msg_99.mensagem()
    if(grp_sub_div.__sizeof__() > 0):
        grupo_sub_div.grupo_sub_div()
    if(kt.__sizeof__() > 0):
        kit.kit()
    if(grup.__sizeof__() > 0):
        grupo.grp()
    if(campanh.__sizeof__() > 0):
        campanha.campanha()
    if(aplic_prod.__sizeof__() > 0):
        aplic_produto.aplic_produto()
    if(empre.__sizeof__() > 0):
        empresa.empresa()

    

