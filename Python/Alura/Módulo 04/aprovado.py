soma = 0

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota
media = soma/3

if media >= 7:
    condicao = "aprovado"
    if media >= 9:
        status = "excelente"
    else:
        status = "bom"
else:
    if media >= 5:
        condicao = "de recuperação"
        status = "bons estudos"
    else:
        condicao = "reprovado"
        status = "se esforce mais"

print(f"A média das notas é de {media:.2f}. Você está {condicao}, {status}.")