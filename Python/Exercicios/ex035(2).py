#Crie um programa que receba três retas e verifique se elas formam um triângulo.

vermelho = '\033[1;31m'
verde = '\033[1;32m'
azul = '\033[1;34m'
magenta = '\033[1;35m'
ciano = '\033[1;36m'
amarelo = '\033[1;33m'
reset = '\033[m'

linha = '-=*'*20
print(f'{verde}{linha}{reset}')
print(f'{azul}Analisador de trângulos{reset}'.center(len(linha)))
print(f'{ciano}Informe os segmentos ou pressione 0 para sair:{reset}'.center(len(linha)))

while True:

    r1 = float(input(f'{vermelho}Primeiro segmento: {reset}'))
    if r1 == 0:
        print(f'{amarelo}Você está saindo do programa. Até logo!!!{reset}')
        break
    r2 = float(input(f'{vermelho}Segundo segmento: {reset}'))
    if r2 == 0:
        print(f'{amarelo}Você está saindo do programa. Até logo!!!{reset}')
        break
    r3 = float(input(f'{vermelho}Terceiro segmento: {reset}'))
    if r3 == 0:
        print(f'{amarelo}Você está saindo do programa. Até logo!!!{reset}')
        break
    
    if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
        print(f'{magenta}As retas {r1}, {r2} e {r3} formam um triângulo.{reset}')
    else:
        print(f'{magenta}As retas {r1}, {r2} e {r3} não formam um triângulo.{reset}')