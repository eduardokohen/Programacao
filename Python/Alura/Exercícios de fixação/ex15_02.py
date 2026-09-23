pares = []
impares = []
i = 1

while True:
    numero = int(input(f"Digite o {i}º número inteiro: "))

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    parada = str(input(("Deseja inserir mais um número? (s/n) "))).lower()
    i += 1
    if parada != "s":
        break
    

texto = f"""
Números pares: {pares}
Números ímpares: {impares}
"""

print(texto)