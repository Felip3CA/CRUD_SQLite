import sqlite3
import streamlit as st
#Etapa 1 - Criação do Banco e Tabela

st.set_page_config(page_title="Biblioteca", page_icon="Biblioteca")
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



#Etapa 6 - Menu Interativo
while True:
    set.button("Seja bem-vindo a biblioteca!")
    menu = st.text_input("Me diga. O que vai fazer hoje?" \
        "(digite" \
        "\n 1 - Função de Cadastro" \
        "\n 2 - Listagem de Livros" \
        "\n 3 - Atualização de Disponibilidade" \
        "\n 4 - Remoçao de Livros)  " \
        "\n Qual será:  ")


    #Etapa 2 - Função de Cadastro
if menu == "1":
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
            st.button(f"Erro ao tentar cadastrar livro: {erro}")
    finally:
            # Sempre fechar a conexão, independentemente de sucesso ou erro
            if conexao:
             conexao.close()

            titulo = st.text_input("Qual o nome do livro que deseja cadastrar:  ")
            autor = st.text_input(f"Qual o autor do livro - |{titulo}|: ")
            ano = st.text_input(f"Qual o ano do livro - |{titulo}|: ")

            cadastrar_livro(titulo, autor, ano)
            


        #Etapa 3 - Listagem de Livros
    elif menu == "2":
  def.listar_livros():
                 try:
                    conexao = sqlite3.connect("biblioteca.db")
                    cursor = conexao.cursor()
                    cursor.execute("SELECT * FROM livros")
                    #fetchall traz todas as linhas da consulta
                    for linha in cursor.fetchall():
                        st.button(f"ID {linha[0]} | TÍTULO {linha[1]} | AUTOR {linha[2]} | ANO {linha[3]} | DISPONIBILIDADE {linha[4]}")

 except Exception as erro:
                    st.button(f"Erro ao tentar listar os livros: {erro}")
                    


        #Etapa 4 - Atualização de Disponibilidade 
elif menu == "3":
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
                     st.button("Acho que você fez algo diferente aqui.")
                    

                        # Atualiza o campo 'disponivel' no banco de dados
                    cursor.execute("UPDATE agendamentos SET disponivel = ? WHERE id = ?", (novo_status, id_livro))

                except Exception as erro:
                    st.button(f"Erro ao tentar atualizar livro: {erro}")
                finally:
            # Commit da mudança
                  conexao.commit()

            # Exibe o commit esperado

                  conexao.close()
            




        #Etapa 5 - Remoção de Livros
elif menu == "4":
 deletar_livro(id_livro):
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
                        st.button("Livro removido com sucesso!")
                    else:
                        st.button("Nenhum livro encontrado com o ID fornecido.")

except Exception as erro:
                    # Caso ocorra algum erro relacionado ao banco de dados
                    st.button(f"Erro ao tentar excluir livro: {erro}")

finally:
                    # Sempre fechar a conexão, independentemente de sucesso ou erro
                    if conexao:
                        conexao.close()

            # Solicitando o ID do livro para deletar

deletar = st.text_input("Digite o id do livro que deseja deletar: ")
deletar_livro(deletar)
            
else:
st.button("Opção não encontrada!")
            









