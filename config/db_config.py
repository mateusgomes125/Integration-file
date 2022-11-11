import psycopg2

endereco = ''
banco = ''
usuario = ''
senha = 'postgres'
porta = '5432'
sslmode = 'require'

conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(endereco, usuario, banco, senha, sslmode)

def connect_db():
    try:
        return psycopg2.connect(conn_string)
        # print("unable to connect to the database.")
        # cursor = conn.cursor()
    except psycopg2.DatabaseError as e:
        print(e)
def disconnect_db(conn):
    try:
        conn.close()
    except psycopg2.DatabaseError as e:
        print(e)

def execute_query(conn, query):
    try:
       cur = conn.cursor()
       res = cur.execute(query)
       cur.close()
       disconnect_db(conn)
       return res
    except psycopg2.DatabaseError as e:
        print(e)
    
