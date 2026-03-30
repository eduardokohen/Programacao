basal = 1250
p1 = 1.15
p2 = 1.1

while True:
    salario = float(input('Informe o salário ou pressione 0 para sair: R$ '))

    if salario == 0:
        print('Você está saindo do aplicativo. Até logo!!!')
        break
    elif salario <= basal:
        salario = salario*p1
    else:
        excedente = salario - basal
        salario = basal*p1 + excedente*p2
    print(f'O salário aumentado é de R$ {salario:.2f}')