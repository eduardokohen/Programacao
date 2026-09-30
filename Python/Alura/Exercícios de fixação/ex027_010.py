idades = []

for i in range(9):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    idades.append(idade)

maiores = [idade for idade in idades if idade >= 18]
menores = [idade for idade in idades if idade < 18]

texto = f"""
Todas as idades: {idades}
Idades maiores de 18: {maiores}
idades menores de 18: {menores}
"""

print(texto)