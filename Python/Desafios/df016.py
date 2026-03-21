#Faça um programa que peça um número e mostre sua tabuada usando o laço de repetição

n = int(input('Digite um número para calcular a tabuada: '))

for i in range(1,11):
    print('{} x {} = {}'. format(n, i, n*i))