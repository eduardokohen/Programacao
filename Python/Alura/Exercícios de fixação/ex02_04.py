soma = 0
i = 0
notas = []

nome = str(input("Informe o nome do aluno: "))

while True:
    nota = float(input(f"Informe a {i+1}ª nota: "))
    soma += nota
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
else:
    condicao = "aprovado(a)"


print(f"As notas de {nome} são: {notas}")
print(f"A média das notas de {nome} é de: {media:.2f}.")
print(f"{nome} está {condicao}.")
if media >= 9:
    print(f"Parabéns! Com uma média de {media} você foi muito bem!")