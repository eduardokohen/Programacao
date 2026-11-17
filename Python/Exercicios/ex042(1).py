lados = []

for i in range(3):
    lado = float(input(f"Informe o comprimento do {i+1}º segmento: "))
    lados.append(lado)

if (lados[0] + lados[1] > lados[2] and
lados[0] + lados[2] > lados[1] and
lados[1] + lados[2] > lados[0]):

    if lados[0] == lados[1] == lados[2]:
        tipo = "equilátero"
    elif lados [0] == lados[1] or lados[0] == lados[2] or lados [1] == lados[2]:
        tipo = "isóceles"
    else:
        tipo = "escaleno"

    print(f"Os segmentos {lados[0]}, {lados[1]} e {lados[2]} formam um triângulo {tipo}.")

else:
    print(f"Os segmentos {lados[0]}, {lados[1]} e {lados[2]} não formam um triângulo.")