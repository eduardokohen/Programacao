notas = []

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

soma = 0

for numero in notas:
    soma = soma + numero

media = soma/len(notas)

print(media)