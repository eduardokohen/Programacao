#Faça um programa que leia uma temperatura em °C e converta para rankine, farenheit e kelvin

tc = float(input('Informe a temperatura em °C: '))

tk = tc+273.15
tf = 9/5*tc + 32
tr = 9/5*tk

print('A temperatura de {:.2f}°C equivale a {:.2f}°F, {:.2f}K e {:.2f}R'.format(tc, tf, tk, tr))