#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Quem ganhar menos de 1250 reais terá 10% de aumento. Quem ganhar menos, 15%.

sal = float(input('Informe o salário: '))
corte = 1250

if sal > corte:
    salr = sal * 1.1
    print(f'O salário reajustado é de R${salr:.2f}.')
else:
    salr = sal * 1.15
    print(f'O salário reajustado é de R${salr:.2f}')