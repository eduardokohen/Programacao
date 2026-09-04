#Crie um programa que classifica uma nota. Se a nota for >= 10,
#excelente. >=7 - bom. >= 5: regular. < 5 - insuficiente.

soma = 0

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota

media = soma/3

if media >= 9:
    condicao = "excelente"
elif media >= 7:
    condicao = "boa"
elif media >= 5:
    condicao = "regular"
else:
    condicao = "insuficiente"

print(f"A média das notas é de {media:.2f}. Sua média foi {condicao}.")