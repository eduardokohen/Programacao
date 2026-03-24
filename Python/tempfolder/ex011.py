#Crie um programa que recebe a altura e largura de uma parede, calcule a área e diga quanta tinta é necessária para pintar

l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))

A = h*l
p = A/2

print('A área da parede é {:.2f} m². Serão necessários {:.2f} litros de tinta para pintar.'.format(A, p))