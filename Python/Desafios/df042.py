#Crie um programa que verifica se um número é par ou ímpar.
#Se ele for par, informe. Se for ímpar, verifique se é divisível por 3. 
#Caso seja divisível por 3, informe. Caso não seja, diga que não é.

num = int(input('Digite um número inteiro qualquer: '))

if num % 2 == 0:
    print('O número {} é par!'.format(num))
else:
    if num % 3 == 0:
        print('O número {} é ímpar e divisível por 3!'.format(num))
    else:
        print('O número {} é ímpar e não é divisível por 3!'.format(num))