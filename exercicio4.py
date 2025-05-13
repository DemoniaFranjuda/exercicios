def calcularmedia(numeros):
    total = 0
    
    for numero in numeros:
        total += numero

    media = total / len(numeros) if numeros else 0 
   
    return media