while True:

    num1 = int(input('Digite o primeiro número inteiro ou 0 para sair: '))

    if num1 == 0:
        print('Você está saindo do programa. Até logo!!!')
        break
    
    num2 = int(input('Digite o segundo número inteiro: '))
    num3 = int(input('Digite o terceiro número inteiro: '))

    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)

    print(f'O maior número é {maior}.')
    print(f'O menor número é {menor}.')