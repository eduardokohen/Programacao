num = int(input('Digite um número inteiro: '))

if num % 2 != 0:
    print('O númmero par vizinho a {} é {}'.format(num, num + 1))

else:
    print('O número {} é par.'.format(num))