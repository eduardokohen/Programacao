casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa/(anos*12)
minimo = salario*0.3
print(f'Para pagar uma casa de {casa:.2f} em {anos} anos',end=' ')
print(f'a prestação será de {prestacao:.2f}')

if prestacao <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')