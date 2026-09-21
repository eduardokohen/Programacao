num = int(input("Digite um número inteiro: "))

for linha in range(3):
    for coluna in range(4):
        print(num, end=" ")
        num += 1
    print()