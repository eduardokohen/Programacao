media = float(input("Informe a média do aluno: "))
nome = str(input("Digite o nome do aluno: ")).title()

if media < 4:
    situacao = "reprovado"
elif media < 6:
    situacao = "de recuperação"
else:
    situacao = "aprovado"

print(f"A média do aluno {nome} é de {media}. {nome} está {situacao}.")