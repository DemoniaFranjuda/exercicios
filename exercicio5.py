from exercicio4 import calcularmedia

alunos = []

def obter_dados_aluno():
   nome_aluno = input("Informe o Nome Completo do Aluno: ")
   email_aluno = input("Informe o Email do Aluno: ")
   serie_aluno = input("Informe a Série do Aluno: ")
   nota01_aluno = int(input("Informe a Primeira Nota do Aluno: "))
   nota02_aluno = int(input("Informe a Segunda Nota do Aluno: "))
   nota03_aluno = int(input("Informe a Terceira Nota do Aluno: "))

   return cadastrar_aluno(nome_aluno, email_aluno, serie_aluno, nota01_aluno, nota02_aluno, nota03_aluno)

def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):


    notas = [nota01, nota02, nota03]
    
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "notas": notas,
        "media": calcularmedia(notas)
   
    }

    alunos.append(aluno)

   
    return alunos



def mostrar_dados_alunos(dados_alunos):
 for aluno in dados_alunos:
    print(f"Nome do Aluno: {aluno["nome"]}")

 return

def iniciar_sistema():
   while True:
      print("="*80)
      print("Opção 1 => Mostrar lista de Alunos Cadastrados.")
      print("Opção 2 => Cadastrar aluno.")
      print("Opção 3 => Sair do sistema.")
      print("="*80)

      opcao = input("Escolha uma das opções acima: ")

      iniciar_sistema() 