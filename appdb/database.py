import sqlite3

#Conectando ao banco
conn = sqlite3.connect("appmobile.db", check_same_thread=False)
cursor = conn.cursor()

#Criar uma tabela no banco
def tabela_user():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login CHAR(20),
            nome CHAR(50),
            idade INTEGER,
            cpf CHAR(15),
            senha CHAR(20),
            oab CHAR(8)
        );
    '''
    )
    conn.commit()