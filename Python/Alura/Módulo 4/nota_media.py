notas = []

# Insere 6 notas na lista
for i in range(6):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

soma = 0
contador = 0

# Percorre a lista
for nota in notas:

    # Verifica se a nota é inválida
    if nota > 10 or nota < 0:
        print(f"Nota {nota} é inválida.")
        continue

    # Se chegou aqui, a nota é válida
    soma += nota
    contador += 1

# Calcula a média apenas das notas válidas
if contador > 0:
    media = soma / contador
    print(f"\nA média das notas válidas é: {media:.2f}")
else:
    print("\nNenhuma nota válida foi informada.")