matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite o número da posição: [{i} {j}] "))
        linha.append(numero)
    
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento, end = " ")
    print()