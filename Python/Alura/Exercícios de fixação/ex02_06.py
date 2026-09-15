notas = []
i = 1

nome = str(input("Informe o nome do aluno: "))

while True:
    nota = float(input(f"Informe a {i}ª nota: "))
    notas.append(nota)
    i += 1

    inserir = str(input(f"Deseja inserir uma {i}ª nota? ")).lower()
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
    condicao = "aprovado(a) com louvor"

print(f"As notas de {nome} são: {notas}.")
print(f"A média das notas é de {media:.2f}.")
print(f"{nome} foi {condicao}.")