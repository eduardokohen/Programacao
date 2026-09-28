notas = []

for i in range(8):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

soma = sum(notas)
media = soma/len(notas)

texto = f"""
Notas: {notas}
Soma: {soma:.2f}
Média: {media:.2f}
"""

print(texto)