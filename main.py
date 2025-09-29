import sqlite3
#Etapa 1 - Criação do Banco e Tabela
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


#Etapa 2 - Função de Cadastro
def cadastrar_livro(titulo, autor, ano, disponivel="Sim"):
    try:
        # Conectando ao banco de dados
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO livros (título, autor, ano, disponivel)
        VALUES (?, ?, ?, "Sim")                          
        """,
        (titulo,autor, ano)
        )
        conexao.commit()
    except Exception as erro:
        # Caso ocorra algum erro relacionado ao banco de dados
        print(f"Erro ao tentar cadastrar livro: {erro}")
    finally:
        # Sempre fechar a conexão, independentemente de sucesso ou erro
         if conexao:
            conexao.close()

titulo = input("Qual o nome do livro que deseja cadastrar:  ")
autor = input(f"Qual o autor do livro - |{titulo}|: ")
ano = int(input(f"Qual o ano do livro - |{titulo}|: "))

cadastrar_livro(titulo, autor, ano)


#Etapa 3 - Listagem de Livros

def listar_livros():
    try:
        cursor.execute("SELECT * FROM alunos")
        #fetchall traz todas as linhas da consulta
        for linha in cursor.fetchall():
            print(f"ID {linha[0]} | TÍTULO {linha[1]} | AUTOR {linha[2]} | ANO {linha[3]}")

        livro = input("Qual curso você deseja ver os alunos: ")
        #Selecionando apenas os alunos do curso Computação
        cursor.execute("SELECT nome, idade FROM alunos WHERE curso = ?", (livro,) )
        for linha in cursor.fetchall():
            print(linha)
    except Exception as erro:
        print(f"Erro ao tentar listar os livros: {erro}")

#Etapa 4 - Atualização de Disponibilidade:
