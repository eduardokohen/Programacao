soma = 0
notas = []
inserir = "s"
i = 0
nome = str(input("Informe o nome do aluno: "))

while inserir == "s":
    nota = float(input(f"informe a {i+1}ª nota: "))
    notas.append(nota)
    i += 1
    soma += nota

    inserir = str(input("Deseja inserir mais uma nota? (S/N): ")).lower()
    if inserir == "n" or inserir == "N":
        break

media = soma/len(notas)

if nota < 5: 
    condicao = "reprovado"
elif nota < 7:
    condicao = "de recuperação"
else:
    condicao = "aprovado"

print(f"Notas de {nome.title()}: {notas}")
print(f"A média das notas de {nome.title()} foi de {media:.2f}.")
print(f"{nome.title()} está {condicao}")