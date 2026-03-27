num = int(input('Digite um número para verificar se é par ou ímpar: '))


while (num <= 0):
    print('Número inválido! Digite um número maior que 0!')
    num = int(input('Digite novamente: '))

if (num > 0 and num % 2 == 0):
    print(f'O número {num} é par.')

elif(num > 0 and num % 2 != 0):
    print(f'O número {num} é impar!')