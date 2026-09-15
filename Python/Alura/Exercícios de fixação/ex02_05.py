i = 0
notas = []

nome = str(input("Informe o nome do aluno: "))

while True:
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)
    i += 1

    inserir = str(input("Deseja inserir mais uma nota? (s/n) ")).lower()
    if inserir == "n":
        break

media = sum(notas)/len(notas)


if media < 5:
    condicao = "reprovado(a)"
elif media < 7:
    condicao = "de recuperação"
elif media <= 8:
    condicao = "aprovado"
else:
    condicao = "aprovado com laudes"

print(f"As notas de {nome} são: {notas}")
print(f"A média das notas de {nome} é de: {media}")
print(f"{nome} está {condicao}.")