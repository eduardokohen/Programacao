azul = '\033[34m'
vermelho = '\033[31m'
verde = '\033[32m'
reset = '\033[m'

velocidade = float(input(f'{azul}Qual é a velocidade do seu carro? {reset}'))

limite = 80

if velocidade <= limite:
    print(f'{verde}Dirija com segurança! Tenha um bom dia!{reset}')
else:
    print(f'{vermelho}MULTADO! Você excedeu o limite permitido que é de {limite:.2f} km/h.{reset}')
    multa = 7*(velocidade - limite)
    print(f'{vermelho}Você terá que pagar uma multa de R$ {multa:.2f}.{reset}')
    print(f'{verde}Tenha um bom dia! Dirija com segurança!{reset}')