import json
import os

agendamentos = "cadastro_de_agendamentos.json"

def carregar_dados():
    if os.path.exists(agendamentos):
        with open(agendamentos, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def obter_dados(): 
    nome = input("Informe o nome do cliente: ")
    servico = input("Informe o serviço desejado: ")
    data = input("Informe a data do agendamento: ")
    horario = input("Informe o horário do agendamento: ")
    observacoes = input("Informe se há observações/especificações: ")

    data_agendamentos ={
        "nome": nome,
        "servico": servico ,
        "data": data,
        "horario": horario, 
        "observacoes": observacoes
    }

    return data_agendamentos

def cadastrar_agendamento(receber_agendamento):
    db_agendamentos = carregar_dados()
    db_agendamentos.append = (receber_agendamento)

    with open(agendamentos, "w", encoding="utf-8") as arq_json:
        json.dump(db_agendamentos, arq_json, indent=4, ensure_ascii=False)

def mostrar_agendamentos(agendamentos):
    if agendamentos:
        for agendamento in agendamentos:
            print(f"""
                  Nome do Cliente {agendamento["nome"]}
                  Tipo de Serviço {agendamento["serviço"]}
                  Data do Agendamento {agendamento["data"]}
                  Horário do Agendamento {agendamento["horario"]}
                  Observações do Cliente {agendamento["observações"]}
            """)
    else:
        print("Não existe nenhum agendamento cadastrado.")

    def iniciar_sistema():
        db_agendamentos = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("Opção 1 - Mostrar agenda completa")
        print("Opção 2 - Cadastrar novo agendamento")
        print("Opção 3 - Sair do sistema")
        print("="*80)

        opcao = input("Escolha uma das opções do menu: ")

        if opcao == "1":
            mostrar_agendamentos(mostrar_agendamentos)
        elif opcao == "2":
            cadastrar_agendamento(obter_dados())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Nenhum agendamento foi cadastrado no momento.")

    iniciar_sistema()