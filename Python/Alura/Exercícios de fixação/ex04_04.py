notas = []
inserir = "s"
nome = input("Digite o nome do aluno: ").title()
i = 1

while inserir == "s":
    nota = float(input(f"Informe a {i}ª nota: "))
    notas.append(nota)
    i += 1

    inserir = input(f"Deseja inserir uma {i}ª nota? (s/n) ").lower()

    if inserir != "s":
        break

media = sum(notas)/len(notas)

if media < 4:
    situacao = "reprovado(a)"
elif media < 6:
    situacao = "de recuperação"
else:
    situacao = "aprovado(a)"

texto = f"""
As notas de {nome} são: {notas}
A média das notas de {nome} é: {media:.2f}
{nome} está {situacao}
"""

print(texto)