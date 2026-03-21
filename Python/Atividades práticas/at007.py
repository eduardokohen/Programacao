#Explorando operadores aritméticos:
a = int(input('Digite um número: '))
b = int(input('Digite outro: '))
soma = a + b
subt = a - b
mult = a * b
div = a / b
pot = a ** b
div_int = a // b
resto = a % b
print('A soma entre {} e {} é {}'.format(a, b, soma))
print('A subtração de {} por {} é {}'.format(a, b, subt))
print('A multiplicação de {} por {} é {}'.format(a, b, mult))
print('A divisão de {} por {} é {}'.format(a, b, div))
print('{} elevado a {} é igual a {}'.format(a, b, pot))
print('A divisão inteira entre {} e {} é {}'.format(a, b, div_int))
print('O resto da divisão de {} por {} é {}'.format(a, b, resto))