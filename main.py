import sqlite3
#Etapa 1
conexao = sqlite3.connect("biblioteca.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
título TEXT NOT NULL,
autor TEXT NOT NULL,
ano INTEGER, 
disponivel TEXT )
""")

print("Consegui fazer alguma coisa!")