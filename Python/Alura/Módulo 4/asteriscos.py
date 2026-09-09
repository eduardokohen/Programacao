linhas = int(input("Informe a quantidade de linhas: "))

for linha in range(1, linhas + 1):
    for valor in range(linha):
        print("*", end = " ")
    print()