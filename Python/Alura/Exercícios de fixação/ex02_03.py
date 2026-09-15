soma = 0
notas = []
nome = str(input("Digite o nome do aluno: ")).title()

for i in range(3):
    nota = float(input(f"Informe a {i+1} nota: "))
    soma += nota
    notas.append(nota)

media = soma/len(notas)

if media < 5:
    condicao = "reprovado"
elif media < 7:
    condicao = "de recuperação"
else:
    condicao = "aprovado"

print(f"As notas de {nome} são: {notas}.")
print(f"A média das notas de {nome} é {media:.2f}")
print(f"{nome} está {condicao}.")