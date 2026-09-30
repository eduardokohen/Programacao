idades = []
maiores = []

for i in range(10):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa>: "))
    idades.append(idade)

for idade in idades:
    if idade >= 18:
        maiores.append(idade)

print(f"Todas as idades: {idades}")
print(f"Idades maiores de 18: {maiores}")