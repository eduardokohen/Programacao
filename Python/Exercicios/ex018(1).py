import math

ang = float(input('Informe a medida do ângulo em graus: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('O ângulo mede {}°, tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente é {:.2f}.' .format(ang, seno, cosseno, tangente))