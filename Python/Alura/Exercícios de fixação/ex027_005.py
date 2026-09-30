idades = []

for i in range(9):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa da lista: "))
    idades.append(idade)

maiores = [idade for idade in idades if idade >= 18]

print(f"Todas as idades: {idades}")
print(f"Maiores de 18: {maiores}")