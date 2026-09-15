num = int(input("Digite um número: "))

numeros = range(0,num+1,1)

for i in numeros:
    if i % 2 != 0:
        continue
    else:
        print(i)