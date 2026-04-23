valor = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe quanto você ganha: R$ '))
prazo = int(input('Informe em quantos meses você pretende pagar: '))
prestacao = valor/prazo

if prestacao > (0.3*salario):
    print('Empréstimo negado por exeder o valor máximo de prestação.')

else:
    print('Empréstimo autorizado! Parabéns!')
    print('Sua prestação será de R$ {:.2f}.'.format(prestacao))