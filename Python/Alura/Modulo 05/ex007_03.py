notas = []

aluno = str(input("Digite o nome do aluno: ")).title()

for i in range(5):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
        else:
            notas.append(nota)
            break

maior = notas[0]
menor = notas[0]
media = sum(notas)/len(notas)

for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

texto = f"""
Aluno: {aluno}
Notas: {notas}
Maior nota: {maior:.2f}
Menor nota: {menor:.2f}
Média: {media:.2f}
"""

print(texto)