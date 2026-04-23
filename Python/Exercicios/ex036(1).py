casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa/(anos*12)
minimo = salario * 0.3

if prestacao <= minimo:
    print('Empréstimo CONCEDIDO!')
    print('O valor da prestação é de {:.2f}, que é menor que {:.2f}'.format(prestacao, minimo))
else:
    print('Empréstimo NEGADO!')
    print('O valor da prestação é de {:.2f} e o máximo permitido é {:.2f}'.format(prestacao, minimo))
