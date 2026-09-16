alunos = []
notas = []

while True:
    aluno = str(input("Digite o nome do aluno ou fim para encerrar: ")).title()

    if aluno == "Fim":
        break

    nota = float(input(f"Digite a nota de {aluno}: "))

    alunos.append(aluno)
    notas.append(nota)

if len(alunos) == 0:
    print("\nNenhum aluno foi cadastrado.")
else:
    media = sum(notas)/len(notas)

    menor = notas[0]
    maior = notas[0]

    for nota in notas:
        if nota < menor:
            menor = nota
        if nota > maior:
            maior = nota

    print("="*60)
    print("NOTAS DOS ALUNOS:".center(60))
    print("="*60)

    for i in range(len(alunos)):
        print(f"{alunos[i]}: {notas[i]:.2f}")
    print("="*60)
    print("RESULTADOS DA TURMA:".center(60))
    print("="*60)

    texto = f""" 
Média da turma = {media}
Maior nota = {maior}    
Menor nota = {menor}
"""
    print(texto)
    print("="*60)