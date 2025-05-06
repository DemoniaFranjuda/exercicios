def calcular_media(numeros):
    total = 0
    for num in numeros:
        total += num
    media = total / len(numeros) if numeros else 0
    return media

lista_numeros = [10, 5, 8, 12, 7]
print(f"A média dos números é: {calcular_media(lista_numeros)}")

