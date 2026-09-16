media = float(input("Digite a média do aluno: "))
nome = str(input("Digite o nome do aluno: ")).title()

if media < 4:
    situacao = "reprovado"
elif media < 6:
    situacao = "de recuperação"
else:
    situacao = "aprovado"

texto = f"""
A média de {nome} é de {media:.2f}.
{nome} está {situacao}.
"""

print(texto)