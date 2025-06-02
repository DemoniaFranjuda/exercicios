import json
import os

veiculos = "cadastro_veiculos.json"

def carregar_dados():
    if os.path.exists(veiculos):
        with open(veiculos, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def obter_dados(): 
    marca = input("Informe a marca do veículo: ")
    modelo = input("Informe o modelo do veículo: ")
    ano = input("Informe o ano do veículo: ")
    cor = input("Informe a cor do veículo")

    data_veiculos ={
        "marca": marca,
        "modelo":modelo,
        "ano": ano,
        "cor": cor
    }
 
def cadastrar_veiculo(receber_veiculo):
    db_veiculos = carregar_dados()
    db_veiculos.append = (receber_veiculo)

    with open(veiculos, "w", encoding="utf-8") as arq_json:
        json.dump(db_veiculos, arq_json, indent=4, ensure_ascii=False)

def mostrar_veiculos(veiculos):
    if veiculos:
        for veiculo in veiculos:
            print(f"""
                  Marca do Veículo {veiculo["marca"]}
                  Modelo do Veículo {veiculo["modelo"]}
                  Ano do Veículo {veiculo["ano"]}
                  Cor do Veículo {veiculo["cor"]}
            """)
    else:
        print("Não existe nenhum carro cadastrado.")

    def iniciar_sistema():
        db_veiculos = carregar_dados()
        db_veiculos.append = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("Opção 1 - Mostrar lista de veículos cadastrados")
        print("Opção 2 - Cadastrar veículo")
        print("Opção 3 - sair do sistema")
        print("="*80)

        opcao = input("Escolha uma das opções do menu: ")

        if opcao == "1":
            mostrar_veiculos(mostrar_veiculos)
        elif opcao == "2":
            cadastrar_veiculo(obter_dados())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Nenhum veículo cadastrado no momento.")

    iniciar_sistema()
 