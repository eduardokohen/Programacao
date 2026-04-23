a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

if a > b:
    print(f'O primeiro valor, {a}, é maior.')
elif b > a:
    print(f'O segundo valor, {b}, é maior.')
else:
    print(f'Os dois valores, {a} e {b}, são iguais.')
