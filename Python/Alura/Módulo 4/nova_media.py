soma = 0
notas = []

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)
    soma += nota

media = nota/len(notas)

print(f"Suas notas foram {notas}.")
print(f"Sua média foi de {media:.2f}")