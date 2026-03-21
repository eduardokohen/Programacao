#Faça um algoritmo que receba um número e calcule sua tabuada

n = int(input('Digite um número para calcular a tabuada: '))

for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, n*i))

#Usando o {:2} reservamos 2 espaços para "i". Assim, os sinais de "=" ficam todos alinhados