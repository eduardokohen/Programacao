#Crie um programa que leia o salário de um trabalhador. Se ele ganhar até 1250, dê um aumento
#de 15%. Se ganhar mais, dê um aumento de 10%.

p1 = 0.15
p2 = 0.10
const = 187.50

while True:

    salario = float(input('Informe o salário ou pressione 0 para sair: '))

    if salario == 0:
        print(f'Você está saindo do programa. Até logo!!!')
        break
    elif salario <= 1250:
        salario = (salario * p1) + salario
    else:
        salario = (salario + const) + salario * p2 #impede que quem está na faixa menor ganhe mais que quem está na maior
    
    print(f'O salário aumentado é de {salario:.2f}.')
