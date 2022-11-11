import re
import os

# Coloque os seus parametros aqui...
diretorio = "/home/veplex05/integration-file"

extensao = ".*638"
  # nesse caso eh vazia
# parteQueSai = "PW0014"
# parteQueSubstitui = "data"

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
                b = os.path.join(diretorio,b)
                os.rename(a,b)

    if os.path.isdir(diretorio) and not os.path.islink(diretorio):
        arquivos = os.listdir(diretorio)
        for arquivo in arquivos:
            newExt = re.compile(extensao).match
            if newExt(arquivo):
                c = os.path.splitext(arquivo)
                b = c[0] + novaExtensao
                a = os.path.join(diretorio,arquivo)
                b = os.path.join(diretorio,b)
                os.rename(a,b)

# Modifica nome
# if os.path.isdir(diretorio) and not os.path.islink(diretorio):
#     arquivos = os.listdir(diretorio)
#     for arquivo in arquivos:
#         print(arquivo)
#         novoNome = str.replace(arquivo, parteQueSai, parteQueSubstitui)
#         fullpathOld = os.path.join(diretorio,arquivo)
#         fullpathNew = os.path.join(diretorio,novoNome)
#         os.rename(fullpathOld, fullpathNew)
