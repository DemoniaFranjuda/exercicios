cliente = []

def obter_dados_cliente():
    nome_cliente = input("informe o nome do cleinte")
    cpf_cliente = int(input("informe o cpf do cliente: "))
    rg_cliente = int(input("informe o rg do cliente: "))
    nascimento_cliente = (input("informe a data de nascimento do cliente: "))
    endereco_cliente = input("informe o endereco do cliente: ")
    cidade_cliente = input("informe a cidade do cliente: ")
    estado_cliente = input("informe o estado do cliente: ")
    telefone_cliente = int(input("informe o telefone do cliente: "))
    celular_cliente = int(input("informe o celualr do cliente:"))
    email_cliente = input("informe o emil do lciente: ")

    cliente = {
        "nome_cliente": nome_cliente,
        "cpf_cliente": cpf_cliente,
        "rg_cliente": rg_cliente,
        "nascimento_cliente": nascimento_cliente,
        "endereco_cliente": endereco_cliente,
        "cidade_cliente": cidade_cliente,
        "estado_cliente": estado_cliente,
        "telefone_cliente": telefone_cliente,
        "celular_cliente": celular_cliente,
        "email_cliente": email_cliente,

    }

    return cliente

def cadastrar_cliente(dados_cliete):
    cliente.append(dados_cliete)

    return cliente

def mostrar_dados_clientes():
    for cliente in obter_dados_cliente:
        print(f"""
              Nome do Cliente: {cliente["nome do cliente"]}
              CPF do Cliente: {cliente["cpf do cliente"]}
              RG do Cliente: {cliente["RG do cliente"]}
              Data de Nascimento do Cliente{cliente["data de nascimento do cliente"]}
              Endereco do Cliente{cliente["endereço do cliente"]}
              Cidade do Cliente{cliente["cidade do cliente"]}
              Estado do Cliente{cliente["estado do cliente"]}
              Telefone do Cliente{cliente["telefone do cliente"]}
              Celular do Cliente{cliente["celular do cliente"]}
              """)
        
def iniciar_sistema():
            while True:
                print("")
                print("="*80)
                print("Opcao 1 - Mostrar Lista de Clientes")
                print("Opcao 2 - Cadastrar Clientes")
                print("Opcao 3 - Sair do Sistema.")
                print("="*80)

                opcao = input("Escolha uma das opções do Menu: ")

                if opcao == "1":
                    mostrar_dados_clientes(cliente)
                elif opcao == "2":
                    cadastrar_cliente(obter_dados_cliente())
                elif opcao == "3":
                    print("Sistema Finalizado")
                    break
                else:
                    print("Opcao invalida, escolha uma das opções no menu.")
iniciar_sistema()