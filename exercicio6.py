def cadastrar_filmes(nome,
    descricao, 
    classificacao, 
    categoria01, 
    categoria02, 
    categoria03 ):
    lista = []
    discionario = {
        "nome" : nome, 
        "descricao" : descricao,
        "classificacao" : classificacao,
        "categorias" : [categoria01, categoria02, categoria03]
    }
    lista.append(discionario)
    return discionario

print(cadastrar_filmes("Coraline", 
    "O filme conta a história de Coraline Jones, uma menina entediada em sua nova casa, que encontra uma porta secreta que a leva a um mundo paralelo. Neste mundo, aparentemente perfeito, ela encontra versões melhoradas de seus pais, que, no entanto, a tentam aprisionar. A trama explora temas como o desejo de uma vida melhor, a dualidade da realidade e da fantasia, e a importância da família. ", 
    "10", 
    "Animação ", 
    "Fantasia",
    "Terror"
    ))