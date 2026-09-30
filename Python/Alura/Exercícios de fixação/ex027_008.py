idades = []
maiores = []
menores = []

for i in range(9):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    idades.append(idade)

for idade in idades:
    if idade >= 18:
        maiores.append(idade)
    else:
        menores.append(idade)

texto = f"""
Todas as idades: {idades}
Idades maiores de 18: {maiores}
Idades menores de 18: {menores}
"""

print(texto)