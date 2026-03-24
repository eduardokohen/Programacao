#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#ex: digite um número: 1834 unidade: 4, dezena: 3, centena: 8, milhar:1

n1 = str(input('Digite um número de 0 a 9999: ')).zfill(4)

print('Unidade: {}'.format(n1[3]))
print('Dezena: {}'.format(n1[2]))
print('Centena: {}'.format(n1[1]))
print('Milhar: {}'.format(n1[0]))