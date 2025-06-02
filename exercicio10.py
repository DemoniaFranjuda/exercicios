import json
import os

filmes = 'cadastro_filmes.json'

def carregar_dados(receber_filmes):
    if os.path.exists(filmes):
        with open(filmes, "r", encondig="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
def obter_dados():
    nome = input("Informe o nome do filme: ")
    classificacao = input("Informe a classificação do filme: ")
    descricao = input("Informe a descrição do filme:")
    categoria = input("Informe a categoria: ")

    data_filmes ={
        "nome": nome,
        "classificação": classificacao,
        "descrição": descricao,
        "categoria": categoria
    }
 
def cadastrar_filme(receber_filmes):
    db_filmes = carregar_dados()
    db_filmes.append = carregar_dados(receber_filmes)

    with open(filmes, "w", encoding="utf-8") as arq_json:
        json.dump(db_filmes, arq_json, indent=4, ensure_ascii=False)

def mostrar_filmes(filmes):
    if filmes:
        for filme in filmes:
            print(f"""
                  Nome do filme {filme["nome_filme"]}
                  Classificação do filme {filme["classificacao"]}
                  Descrição do filme {filme["descricao"]}
                  Categoria do filme {filme["categoria"]}
            """)
    else:
        print("Não existe nenhum filme cadastrado.")

def iniciar_sistemar(receber_filmes):
    db_filmes = carregar_dados()
    db_filmes.append = carregar_dados(receber_filmes)

    while True:
        print("")
        print("="*80)
        print("Opção 1 - Mostrar lista de filmes")
        print("Opção 2 - Cadastrar filme")
        print("Opção 3 - sair do sistema")
        print("="*80)

        opcao = input("Escolha uma das opções do menu: ")

        if opcao == "1":
            mostrar_filmes(db_filmes)
        elif opcao == "2":
            cadastrar_filme(obter_dados())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção invalida, escolha uma das opções do menu.")
iniciar_sistema()
