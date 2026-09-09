alunos = []

for i in range(4):
    aluno = str(input(f"Informe o nome do {i+1}º aluno: "))
    alunos.append(aluno)

for i in range(len(alunos)):
    print(i+1, end = " ")
    print(alunos[i], end = " ")