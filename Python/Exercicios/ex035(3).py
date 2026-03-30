#Crie um programa que receba três retas e verifique se elas formam um triângulo.

vermelho = '\033[1;31m'
verde = '\033[1;32m'
azul = '\033[1;34m'
magenta = '\033[1;35m'
ciano = '\033[1;36m'
amarelo = '\033[1;33m'
reset = '\033[m'

linha = '-='*30
print(f'{magenta}{linha}{reset}')
titulo = 'Bem vindo ao verificador de triângulos!'.center(len(linha))
print(f'{ciano}{titulo}{reset}')
print(f'{magenta}{linha}{reset}')
subtitulo = 'Informe os segmentos ou pressione 0 para sair:'.center(len(linha))
print(f'{amarelo}{subtitulo}{reset}'.center(len(linha)))

def eh_triangulo(lado):
    return sum(lado) - max(lado) > max(lado)

while True:

    lado =[]

    for i in range(3):
        valor = float(input(f'{verde}{i+1}º segmento: {reset}'))
        lado.append(valor)

        if valor == 0:
            print(f'{vermelho}Você está saindo do programa. Até logo!!!{reset}')
            exit()
    
    triangulo = eh_triangulo(lado)

    if triangulo:
        print(f'{azul}Os segmentos {lado[0]}, {lado[1]} e {lado[2]} formam um triângulo.{reset}')
    else:
        print(f'{azul}Os segmentos {lado[0]}, {lado[1]} e {lado[2]} não formam um triângulo.{reset}')