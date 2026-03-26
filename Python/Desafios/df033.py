#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = int(input('Digite um número de 0 a 9999: '))

m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print(f'Unidade: {u}; \nDezena: {d}; \nCentena: {c}; \nMilhar: {m}')