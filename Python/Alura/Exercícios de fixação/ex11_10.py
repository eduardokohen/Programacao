notas = []

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

maior = notas[0]
menor = notas[0]
media = sum(notas)/len(notas)

for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

texto = f"""
As notas são: {notas}
A maior nota é: {maior}
A menor nota é: {menor}
A média das notas é: {media:.2f}
"""

print(texto)