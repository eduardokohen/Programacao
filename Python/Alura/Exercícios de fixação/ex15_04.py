pares = []
impares = []
i = 1

while True:
    num = int(input(f"Informe o {i}º número inteiro: "))

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