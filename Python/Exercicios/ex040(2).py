nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1+nota2)/2
print(f"Tirando {nota1} e {nota2}, a média é {media:.2f}.")

if media < 5:
    situacao = "reprovado"
elif media < 7:
    situacao = "de recuperação"
else:
    situacao = "aprovado"

print(f"O aluno está {situacao}.")