numeros = []
fator = range(1,11)

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número da tabuada: "))
    numeros.append(numero)

for numero in numeros:
    for n in fator:
        multiplicacao = numero*n
        print(f"A multiplicação de {numero} x {n} = {multiplicacao}.")