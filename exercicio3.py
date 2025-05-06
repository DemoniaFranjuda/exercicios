def verificar_idade(nome, idade):
    if idade >= 18:
        return f"{nome}, você é maior de idade."
    else:
        return f"{nome}, você é menor de idade."

print(verificar_idade("Demonia", 666)) 
print(verificar_idade("Franjuda", 16)) 
