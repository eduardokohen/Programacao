num = int(input("Digite um número: "))

numeros = range(0, num, 1)

for i in numeros:
    if i > 5:
        print(i)
        break
print("Busca finalizada.")