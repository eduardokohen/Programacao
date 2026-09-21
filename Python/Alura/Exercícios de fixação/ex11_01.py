notas = []

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

maior = notas[0]
menor = notas[0]

for nota in notas:
    if maior < nota:
        maior = nota
    if menor > nota:
        menor = nota

media = sum(notas)/len(notas)

texto = f"""
As notas são: {notas}
A maior nota é: {maior}
A menor nota é: {menor}
A média das notas é: {media:.2f}
"""

print(texto)