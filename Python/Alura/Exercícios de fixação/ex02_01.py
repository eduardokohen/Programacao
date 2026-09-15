soma = 0
notas = []
nome = str(input("Digite o nome do aluno: "))

for i in range(3):
    nota = float(input(f"Informe a {i+1}ª nota: "))
    notas.append(nota)
    soma += nota

media = soma/len(notas)

if media < 5:
    condicao = "reprovado"
elif media < 7:
    condicao = "de recuperação"
else:
    condicao = "aprovado"

print(f"A média das notas de {nome.title()} é de {media:.2f}.")
print(f"{nome.title()} está {condicao}.")