notas = []

for i in range(6):
    nota = float(input(f"Informe a {i+1}ª nota: "))
    notas.append(nota)

notas_aprovadas = []
notas_reprovadas = []

for nota in notas:
    if nota >= 7:
        notas_aprovadas.append(nota)
    else:
        notas_reprovadas.append(nota)

print(f"Notas aprovadas: {notas_aprovadas}.")
print(f"Notas reprovadas: {notas_reprovadas}.")