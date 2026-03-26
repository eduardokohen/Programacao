salario = float(input('Informe o salário para calcular o IRPF: '))

isento = 2428.80
primeira = 2826.65
segunda = 3751.05
terceira = 4664.68

if salario <= isento:
    irpf = 0 * isento

elif isento < salario <= primeira:
    irpf = 0.075 * (salario - isento)

elif primeira < salario <= segunda:
    irpf = ((primeira - isento) * 0.075) + ((salario - primeira) * 0.15)

elif segunda < salario <= terceira:
    irpf = ((primeira - isento) * 0.075) + ((segunda - primeira) * 0.15) + ((salario - segunda)*0.225)

else:
    irpf = ((primeira - isento) * 0.075) + ((segunda - primeira) * 0.15) + ((terceira - segunda) * 0.225) + ((salario - terceira)*0.275)

print('O imposto de renda incidente sobre R$ {:.2f} é de R${:.2f}'.format(salario, irpf))