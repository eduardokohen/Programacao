#Faça um programa que leia a largura e a altura de uma parede, calcule a área e diga quantos litros de tinta são
#necessários para pintar a parede, sabendo que cada litro de tinta pinta 2m²

h = float(input('Qual é a altura da parede? '))
l = float(input('Qual é a largura da parede? '))
area = h*l
litros = area/2

print('Sua parede tem uma área de {:.2f} m². Para pintá-la serão necessários {:.2f} l de tinta.'.format(area, litros))
print(f'Sua parede tem {area:.2f} m². Para pintá-la serão necessários {litros:.2f} l de tinta.')