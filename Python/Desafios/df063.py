#Refaça o desafio do triângulo, mas dessa vez, além de dizer se três retas formam um triângulo
#informe também se ele é equilátero, isóceles ou escaleno

lado = []

for i in range(3):
    valor = float(input('Informe a medida do {}º lado: '.format(i+1)))
    lado.append(valor)

maior = lado[0]

if (lado[0] + lado[1] > lado[2] and
    lado[0] + lado[2] > lado[1] and
    lado[1] + lado[2] > lado[0]):
    if (lado[0] == lado[1]) and (lado[1] == lado[2]):
        tipo = 'isóceles'
    elif (lado[0] == lado[1] or (lado[1] == lado[2]) or (lado[2] == lado[0])):
        tipo = 'equilátero'
    else:
        tipo = 'escaleno'
    print(f'As retas {lado[0]}, {lado[1]} e {lado[2]} formam um triângulo {tipo}.')

else:
    print(f'As retas {lado[0]}, {lado[1]} e {lado[2]} não formam um triângulo')