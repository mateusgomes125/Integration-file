import ssl
from ftplib import FTP_TLS, all_errors

def ftp_connect():
    host = 'sys.oniz.com.br'
    port = 2100
    user = 'ftp_upvendas'
    password = 'ab9012%'

    try:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        if(ssl_context):
            print('CONTEXT CREATED!')
        with FTP_TLS(context = ssl_context) as ftps:
            if(ftps.connect(host, port)):
                print('CONNECTED!')
            if (ftps.sendcmd('USER ' + user) and ftps.sendcmd('PASS ' + password)):
                print('LOGGED IN!')
                ftps.cwd('/PALM/ENVIO')
                print('Diretório atual: ' + ftps.pwd())
                files = ftps.nlst()
                if(files.__sizeof__ > 0):
                     ftps.retrbinary(f'RETR ' + files[0], open(files[0], 'wb').write)
                     ftps.delete(files[0])
                     return files[0]
                else:
                    return False
                # ftps.dir()   
                # commands(ftps)
    except all_errors as e:
        print('Falha ao conectar: ' + e)
        # ftps.quit()
        # print('ftp closed!')