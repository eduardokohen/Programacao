num = int(input('Informe um número inteiro: '))
opcao = int(input('[1] Converter para BINÁRIO \n[2] Converter para OCTAL \n[3] Converter para HEXADECIMAL \n'))

if opcao == 1:
    num2 = (bin(num)[2:])
    condicao = 'binário'
elif opcao == 2:
    num2 = (oct(num)[2:])
    condicao = 'octal'
elif opcao == 3:
    num2 = (hex(num)[2:])
    condicao = 'hexadecimal'
else:
    print('Opção inválida!')
    exit()

print(f'O número {num} em {condicao} é {num2}.')