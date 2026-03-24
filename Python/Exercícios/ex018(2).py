from math import radians, sin, cos, tan

ângulo = float(input('Informe a medida do ângulo em graus: '))
rad = radians(ângulo)
s = sin(rad)
cs = cos(rad)
tg = tan(rad)

print('O ângulo em radianos mede {:.2f}, seu seno vale {:.2f}, seu cosseno vale {:.2f} e sua tangente vale {:.2f}'.format(rad, s, cs, tg))