#crie um programa que peça um ângulo e calcule o seno, cosseno e a tangente.
import math
graus = float(input('Informe um ângulo em graus: '))

teta = math.radians(graus)

seno = math.sin(teta)
cosseno = math.cos(teta)
tangente = math.tan(teta)

print('O ângulo em radianos é {:.2f}. \nSeu seno é {:.2f}.\nSeu cosseno é {:.2f}. \nSua tangente é {:.2f}.'.format(teta, seno, cosseno, tangente))