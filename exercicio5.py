from exercicio4 import calcular_media

def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):
    alunos = []

    notas = [nota01, nota02, nota03]

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "notas": notas,
        "media": calcular_media(notas)
    }

    alunos.append(aluno)

    return alunos