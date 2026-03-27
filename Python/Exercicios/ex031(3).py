ckm1 = 0.5
ckm2 = 0.45
corte = 200

dist = float(input('Informe a distância da sua viagem: '))

if dist <= corte:
    valor = dist*ckm1
else:
    valor = dist*ckm2

print(f'Você está prestes a fazer uma viagem de {dist} km. Parabéns!')
print(f'O valor da sua passagem é de R$ {valor}.')