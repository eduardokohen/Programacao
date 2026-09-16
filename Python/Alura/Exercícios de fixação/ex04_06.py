media = float(input("Digite a média do aluno: "))
nome = str(input("Digite o nome do aluno: ")).title()

if media < 4:
    situacao = "reprovado"
elif media < 6:
    situacao = "de recuperação"
else:
    situacao = "aprovado"

texto = f"""
A média do aluno {nome} é de {media}.
O aluno {nome} está {situacao}.
"""

print(texto)