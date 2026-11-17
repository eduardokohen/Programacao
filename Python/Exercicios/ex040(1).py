aluno = str(input("Digite o nome do aluno: "))

notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas)/len(notas)

if media < 5:
    situacao = "reprovado"
elif media < 7:
    situacao = "de recuperação"
else:
    situacao = "aprovado"

texto = f"""
A média das notas de {aluno} é {media:.2f}.
{aluno} está {situacao}.
"""

print(texto)