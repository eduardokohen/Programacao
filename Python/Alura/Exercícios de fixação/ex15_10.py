pares = []
impares = []
i = 1

while True:

    num = int(input(f"Digite o {i}º número: "))

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    parada = str(input("Deseja inserir mais um número? (s/n) ")).lower()

    if parada != "s":
        break
    i += 1

texto = f"""
Números pares: {pares}
Números ímpares: {impares}
"""

print(texto)