#Crie um algoritmo que leia um número, mostre seu dobro, seu triplo e a raiz quadrada
x = int(input('Digite um número inteiro: '))
d = x * 2
t = x * 3
sq = x**(1/2)
print('O número digitado foi {}. Seu dobro é {}, seu triplo é {} e a raiz quadrada é {}'.format(x, d, t, sq))