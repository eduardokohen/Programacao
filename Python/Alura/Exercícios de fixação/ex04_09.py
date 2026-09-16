nome = str(input("Digite o nome do aluno: ")).title()
media = float(input("Digite a nota do aluno: "))

if media < 4:
    situacao = "reprovado(a)"
elif media < 6:
    situacao = "de recuperação"
else:
    situacao = "aprovado(a)"

texto = f"""
A média de {nome} é: {media:.2f}.
{nome} está {situacao}.
"""

print(texto)