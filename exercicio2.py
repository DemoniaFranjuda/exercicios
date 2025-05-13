def somar_numeros(lista):
    total = 0
    for numero in lista:
         total += numero
    return total


numeros = [1, 2, 3, 4, 5, 6]
resultado = somar_numeros (numeros)
print(resultado)
