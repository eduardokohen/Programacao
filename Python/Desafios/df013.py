#Crie um programa que leia um número e mostre seu dobro, seu triplo e sua raiz quadrada
n = int(input('Digite um número: '))

d = n*2
t = n*3
r = n**(1/2)

print('O número digitado foi {} \nSeu dobro é {} \nSeu triplo é {} \nSua raiz quadrada é {}'.format(n, d, t, r))