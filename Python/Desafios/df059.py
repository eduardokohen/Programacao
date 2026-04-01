num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    tipo = ' primeiro número é maior'
elif num1 < num2:
    tipo = ' segundo número é maior'
else:
    tipo = 's dois números são iguais'

print('O{}.'.format(tipo))