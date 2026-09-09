notas = []

while True:
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

    continuar = str(input("Deseja adicionar outra nota? (s/n): "))

    if continuar.lower() == "n":
        break

soma = sum(notas)
media = soma/len(notas)

if media >= 9:
    condicao = "Você foi excelente"
elif media >= 7:
    condicao = "Você foi bem"
elif media >= 5:
    condicao = "Você está de recuperação"
else:
    condicao = "Você foi reprovado."
print(f"Sua média foi {media}. {condicao}!")