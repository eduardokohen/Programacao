media = float(input("Informe a média do aluno: "))
nome = str(input("Informe o nome do aluno: "))

if media < 4:
    situacao = "reprovado"
elif media < 6:
    situacao = "de recuperação"
else:
    situacao = "aprovado"

print (f"A média de {nome} foi {media}. {nome} está {situacao}.")