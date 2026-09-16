notas = []
i = 1
nome = str(input("Digite o nome do aluno: "))

while True:
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)
    i += 1

    inserir = str(input(f"Deseja inserir uma {i}ª nota? (s/n) ")).lower()

    if inserir == "n":
        break

media = sum(notas)/len(notas)

if media < 4:
    situacao = "reprovado(a)"
elif media < 6:
    situacao = "de recuperação"
else:
    situacao = "aprovado(a)"

print(f"As notas de {nome} são: {notas}.")
print(f"A média das notas de {nome} é: {media:.2f}.")
print(f"{nome} está {situacao}.")