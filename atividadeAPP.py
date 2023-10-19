import sys

def adicionarAluno():
    id_aluno = int(input("Insira o ID do aluno: "))
    nome = input("Insira nome do aluno: ")
    notas = input("Insira as notas do aluno: ").split()

    notas = [eval(i) for i in notas]
    print(notas)

    print(nome + " adicionado!")

    alunos.append({"id": id_aluno, "nome": nome, "notas": notas})

def exibirAlunos():
    for aluno in alunos:
        print(aluno)

def procurarAluno(id_aluno):
    for aluno in alunos:
        if aluno['id'] == id_aluno:
            print(f"Encontrado: {aluno}")
            return
    print(f"Aluno com o ID {id_aluno} não encontrado!")

def calcularMedia():
    quantidadeDeNotas = 0
    somaDasNotas = 0
    for aluno in alunos:
        print(aluno)
        somaDasNotas += sum(aluno['notas'])
        quantidadeDeNotas += len(aluno['notas'])

    media = somaDasNotas / quantidadeDeNotas

    print(f"A média das notas dos estudantes foi: {media}")

def salvarRegistrosTxt():
    with open('lista_alunos.txt', 'w') as arquivo_de_alunos:
        for aluno in alunos:
            arquivo_de_alunos.write(f"{aluno['id']}, {aluno['nome']}, {aluno['nota']}\n")

def carregarRegistroTxt():
    listaDeRetorno = []
    with open('lista_alunos.txt') as arquivo_de_alunos:
        for line in arquivo_de_alunos:
            aluno = line.split(sep=',')
            for i in range(0, len(aluno)):
                aluno[i] = aluno[i].strip().replace("[", "").replace("]", "")
            listaDeRetorno.append(aluno)

    for lista in listaDeRetorno:
        registroDeAluno = {"id": 0, "nome": "", "notas": []}
        for i in range(0, len(lista)):
            if i == 0:
                registroDeAluno["id"] = int(lista[0])
            elif i == 1:
                registroDeAluno["nome"] = lista[1]
            elif i > 1:
                registroDeAluno['notas'].append(int(lista[i]))
        alunos.append(registroDeAluno)
    print("Carregamento realizado com sucesso!")

alunos = []
while True:
    print(
          "1. Adicionar Aluno\n" +
          "2. Exibir Registro dos Alunos\n" +
          "3. Procurar por um Aluno\n" +
          "4. Calcular Média de Notas\n" +
          "5. Salvar Arquivo\n" +
          "6. Carregar Arquivo\n" +
          "0. Sair")

    opcao = input("Digite sua escolha (0-6): ")

    if opcao == "1":
        adicionarAluno()
    elif opcao == "2":
        exibirAlunos()
    elif opcao == "3":
        procurarAluno (int(input("Digite o ID do aluno que deseja pesquisar: ")))
    elif opcao == "4":
        calcularMedia()
    elif opcao == "5":
        salvarRegistrosEmTxt()
    elif opcao == "6":
        carregarRegistroTxt()
    elif opcao == "0":
        sys.exit()
    else:
        print(f"Opção {opcao} inválida, tente novamente!")
