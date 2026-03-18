<<<<<<< HEAD
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
            login CHAR(20) UNIQUE,
            nome CHAR(50),
            idade INTEGER,
            cpf CHAR(15),
            senha CHAR(20),
            oab CHAR(8)
        );
    '''
    )
=======
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
            login CHAR(20) UNIQUE,
            nome CHAR(50),
            idade INTEGER,
            cpf CHAR(15),
            senha CHAR(20),
            oab CHAR(8)
        );
    '''
    )
>>>>>>> ff2096e020ad99b703ad1bd7097844588e2135c7
    conn.commit()