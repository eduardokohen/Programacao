#Escreva um programa que leia um número inteiro e pela para o usuário escolher qual será
#a base de conversão. 1 para binário, 2 para octal e 3 para hexadecimal

print('-='*30)
print('Bem vindo ao conversor de números!!!'.center(60))
print('-='*30)

while True:
    num1 = int(input('Digite um número inteiro: '))
    opcao = int(input('Digite a opção:\n1 - Binário \n2 - Octal \n3 - Hexadecimal \n0 - Sair\n'))

    if opcao == 0:
        break
    elif opcao == 1:
        num2 = bin(num1)[2:]
        tipo = 'binário'
    elif opcao == 2:
        num2 = oct(num1)[2:]
        tipo = 'octal'
    elif opcao == 3:
        num2 = hex(num1)[2:]
        tipo = 'hexadecimal'
    else:
        print('Opção inválida!')
        continue

    print('O número {} em {} é {}'.format(num1, tipo, num2))