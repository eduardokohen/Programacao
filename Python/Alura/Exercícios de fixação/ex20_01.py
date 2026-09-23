alunos = {}

while True:
    print("\n1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Remover")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")

        notas = []

        for i in range(3):
            nota = float(input(f"Nota {i + 1}: "))
            notas.append(nota)

        alunos[nome] = notas

        print("Aluno cadastrado.")

    elif opcao == "2":
        nome = input("Nome do aluno: ")

        if nome in alunos:
            notas = alunos[nome]
            media = sum(notas) / len(notas)

            print("Notas:", notas)
            print(f"Média: {media:.2f}")

        else:
            print("Aluno não encontrado.")

    elif opcao == "3":
        nome = input("Nome do aluno: ")

        if nome in alunos:
            del alunos[nome]
            print("Aluno removido.")

        else:
            print("Aluno não encontrado.")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")