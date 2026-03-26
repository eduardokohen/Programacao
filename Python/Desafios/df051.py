salario = float(input('Informe o salário para o cálculo do IRPF: '))

faixas = [2428.80, 2826.65, 3751.05, 4664.68]

aliquotas = [0, 0.075, 0.15, 0.225, 0.275]

irpf = 0
limite_anterior = 0

for i in range(len(aliquotas)):
    if i < len(faixas):
        limite_atual = faixas[i]
    else:
        limite_atual = salario
    
    if salario > limite_anterior:
        base_calculo = min(salario, limite_atual) - limite_anterior
        irpf += base_calculo * aliquotas[i]
    
    limite_anterior = limite_atual

print(f'O IRPF para o salário de R${salario:.2f} é de R${irpf:.2f}')