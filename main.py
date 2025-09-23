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
def cadastrar_livro(titulo, autor, ano):
    try:
        # Conectando ao banco de dados
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO livros (título, autor, ano)
        VALUES (?, ?, ?)                          
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
ano = int(input(f"Qual o nome do livro - |{titulo}|: "))

cadastrar_livro(titulo, autor, ano)


#Etapa 3 - Listagem de Livros
