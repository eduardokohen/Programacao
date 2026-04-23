num = int(input('Digite um número inteiro: '))
print('''Escolha uma opção para conversão:
      [1] Converter para BINÁRIO
      [2] Converter para OCTAL
      [3] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    condicao = 'binário'
    num2 = (bin(num)[2:])
elif opcao == 2:
    condicao = 'octal'
    num2 = (oct(num)[2:])
elif opcao == 3:
    condicao = 'hexadecimal'
    num2 = (hex(num)[2:])
else:
    print('Opção inválida!')
    exit()

print(f'O número {num} convertido em {condicao} é {num2}')