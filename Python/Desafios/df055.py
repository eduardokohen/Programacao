#crie um programa que peça ao usuário um número, verifique se é negativo, positivo ou 0 e apresente o resultado

num = int(input('Digite um número inteiro: '))

if num < 0:
    print('O número {} é negativo.'.format(num))
elif num > 0:
    print('O número {} é positivo.'.format(num))
else:
    print('O número é {}'.format(num))