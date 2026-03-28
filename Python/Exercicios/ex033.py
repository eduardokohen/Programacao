#Crie um programa que leia três números e diga:
#Qual é o maior e qual é o menor.

maior = 0
menor = 0

while True:

    num1 = int(input('Digite o primeiro número inteiro (ou 0 para sair): '))
    
    if num1 == 0:
        print('Você está saindo do programa. Até logo!!"')
        break

    num2 = int(input('Digite o segundo número inteiro: '))
    num3 = int(input('Digite o terceiro número inteiro: '))

    if (num1 > num2) and (num1 > num3):
        maior = num1
    elif (num2 > num1) and (num2 > num3):
        maior = num2
    else:
        maior = num3

    if (num1 < num2) and (num1<num3):
        menor = num1
    elif (num2 < num1) and (num2 < num3):
        menor = num2
    else:
        menor = num3

    print(f'O maior número é {maior}.')
    print(f'O menor número é {menor}')