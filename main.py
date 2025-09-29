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

#Etapa 6 - Menu Interativo


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
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM livros")
        #fetchall traz todas as linhas da consulta
        for linha in cursor.fetchall():
            print(f"ID {linha[0]} | TÍTULO {linha[1]} | AUTOR {linha[2]} | ANO {linha[3]} | DISPONIBILIDADE {linha[4]}")

    except Exception as erro:
        print(f"Erro ao tentar listar os livros: {erro}")



#Etapa 4 - Atualização de Disponibilidade: 

def atualizar_disponibilidade(id_livro):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT disponivel FROM biblioteca WHERE id = ?", (id_livro,))
        resultado = cursor.fetchall()

        if resultado:
         disponivel_atual = resultado[0]

# Verifica se o campo é 'Sim' ou 'Não' e faz a troca
         if disponivel_atual == 'Sim':
                novo_status = 'Não'
         elif disponivel_atual == 'Não':
                novo_status = 'Sim'
         else:
          print("Acho que você fez algo diferente aqui.")
          return

            # Atualiza o campo 'disponivel' no banco de dados
        cursor.execute("UPDATE agendamentos SET disponivel = ? WHERE id = ?", (novo_status, id_livro))

    except Exception as erro:
        print(f"Erro ao tentar atualizar livro: {erro}")

# Commit da mudança
conexao.commit()

 # Exibe o commit esperado



 

conexao.close()




#Etapa 5 - Remoção de Livros

def deletar_livro(id_livro):
    try:
        # Conectando ao banco de dados
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        # Deletando o livro com o ID fornecido
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
       
        # Confirmando a alteração
        conexao.commit()

        # Verificando se algum livro foi realmente deletado
        if cursor.rowcount > 0:
            print("Livro removido com sucesso!")
        else:
            print("Nenhum livro encontrado com o ID fornecido.")

    except Exception as erro:
        # Caso ocorra algum erro relacionado ao banco de dados
        print(f"Erro ao tentar excluir livro: {erro}")

    finally:
        # Sempre fechar a conexão, independentemente de sucesso ou erro
        if conexao:
            conexao.close()

# Solicitando o ID do livro para deletar
deletar = input("Digite o id do livro que deseja deletar: ")
deletar_livro(deletar)

# Etapa 6 - Menu Interativo:







