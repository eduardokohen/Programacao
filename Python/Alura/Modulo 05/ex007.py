notas = []
alunos = []

for i in range(3):
    aluno = str(input(f"Digite o nome do {i+1}º aluno: ")).title()
    alunos.append(aluno)

for i in range(3):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)

turma = {}

for i in range(3):
    turma[alunos[i]] = notas[i]

aprovados = {}

for aluno, nota in turma.items():
    if nota >= 7:
        aprovados[aluno] = nota

print(aprovados)