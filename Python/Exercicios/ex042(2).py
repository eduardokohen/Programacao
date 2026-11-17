r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        tipo = "equilátero"
    elif r1 == r2 or r2 == r3 or r1 == r3:
        tipo = "isóceles"
    else:
        tipo = "escaleno"

    print(f"Os segmentos {r1}, {r2} e {r3} formam um triângulo {tipo}.")

else:
    print(f"Os segmentos {r1}, {r2} e {r3} não formam um triângulo.")