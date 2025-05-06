def verificar_idade(nome, idade):
    if idade >= 18:
        return f"{nome}, você é maior de idade."
    else:
        return f"{nome}, você é menor de idade."

nome_usuario = input("Digite seu nome: ")
idade_usuario = input("Digite sua idade: ")

try:
    idade_usuario = int(idade_usuario)
    print(verificar_idade(nome_usuario, idade_usuario))
except ValueError:
    print("Idade inválida! Por favor, digite um número inteiro para a idade.")
    

