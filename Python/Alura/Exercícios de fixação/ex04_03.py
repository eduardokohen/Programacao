notas = []
nome = input("Digite o nome do aluno: ").title()

for i in range (1, 1000, 1):
    nota = float(input(f"Informe a {i}ª nota: "))
    notas.append(nota)

    inserir = input(f"Deseja inserir uma {i+1}ª nota? (s/n) ").lower()

    if inserir == "n":
        break

media = sum(notas)/len(notas)

if media < 4:
    situacao = "reprovado(a)"
elif media < 6:
    situacao = "de recuperação"
else:
    situacao = "aprovado(a)"

texto = f"""
As notas de {nome} são: {notas}.
A média das notas de {nome} é: {media:.2f}.
{nome} está {situacao}.
"""

print(texto)