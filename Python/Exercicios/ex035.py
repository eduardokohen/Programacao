def eh_triangulo(lado):
    if ((lado[0] + lado[1]) > lado[2] and
        (lado[1] + lado[2]) > lado[0] and
        (lado[0] + lado[2]) > lado[1]):
        return True
    else:
        return False

while True:
    
    lado = []

    for i in range(3):
        valor = float(input(f'Informe a medida do {i + 1}º lado ou pressione 0 para sair: '))
        if valor == 0:
            print('Você está saindo do programa. Até logo!!!')
            exit()
        lado.append(valor)
    
    triangulo = eh_triangulo(lado)

    if triangulo:
        print(f'As retas {lado[0]}, {lado[1]} e {lado[2]} formam um triângulo.')
    else:
        print(f'As retas {lado[0]}, {lado[1]} e {lado[2]} não formam um triângulo.')
