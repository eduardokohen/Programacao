#Escreva um programa em python para aprovar o empréstimo para compra de uma casa.
#O programa perguntará o valor da casa, o salário do comprador e em quantos anos ele vai pagaar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário,
#Ou então o empréstimo será negado

valor = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o salário: R$'))
prazo = int(input('Informe o prazo para pagar: '))
prestacao = valor/prazo

if prestacao <= salario*0.3:
    print('Você conseguiu o financiamento! Parabéns!')
    print('Sua prestação será de {}'.format(prestacao))
else:
    print('Empréstimo negado!')