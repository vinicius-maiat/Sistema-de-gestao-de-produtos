# Aqui fica o código que conversa com o banco 

import sqlite3

# função para conectar o banco e criar o banco 

def conectar():
    return sqlite3.connect("banco.db")

# função pra mostrar pro banco como os produtos vão serr armazenados 

def criar_tabela():
    conexao = conectar()

    #O cursor é o objeto que vamos utilizar para mandar comandos SQL para o banco
    cursor = conexao.cursor()

    # tipo um "Execute esssa função no banco"
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()