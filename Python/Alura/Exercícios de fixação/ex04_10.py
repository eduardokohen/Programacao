nome = str(input("Digite o nome do aluno: ")).title()
media = float(input("Digite a média do aluno: "))

if media < 4:
    situacao = "reprovado(a)"
elif media < 6:
    situacao = "de recuperação"
elif media < 8:
    situacao = "aprovado(a)"
else:
    situacao = "aprovado(a) com louvor"

texto = f"""
A média de {nome} = {media}.
{nome} está {situacao}.
"""

print(texto)