#Crie um programa que calcule o IRPF com base no salário e nas faixas salariais.

salario = float(input('Informe o salário para o cálculo do IRPF: '))

f1 = 2428.80
f2 = 2826.65
f3 = 3751.05
f4 = 4664.68

a1 = f1*0
a2 = (f2-f1)*0.075
a3 = (f3-f2)*0.15
a4 = (f4-f3)*0.225
a5 = (salario-f4)*0.275

if salario <= f1:
    irpf = a1

elif f1 < salario <=f2:
    irpf = a1 + (salario - f1)*0.075
elif f2 < salario <= f3:
    irpf = a1 + a2 + (salario - f2)*0.15
elif f3 < salario <= f4:
    irpf = a1 + a2 + a3 + (salario - f3)*0.225
else:
    irpf = a1 + a2 + a3 + a4 + a5

print(f'O IRPF para o salário de R${salario:.2f} é de {irpf:.2f}')