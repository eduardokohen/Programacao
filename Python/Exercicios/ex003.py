#Crie um programa que leia dois números e mostre a soma entre eles
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo valor: '))
s = n1+n2
print('A soma entre {} e {} é igual a {}.'.format(n1, n2, s))
print(f'A soma entre {n1} e {n2} é igual a {s}')
print('A soma entre ' + str(n1) + ' e ' + str(n2) + ' é igual a ' + str(s) + '.')