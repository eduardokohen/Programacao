#Faça um código que calcule o preço de uma passagem. Para viagens de até 200km, R$0,50/km.
#Para viagens de mais de 200km, o preço do km é de R$0,45/km.

dist = float(input('Informe a distância da viagem: '))

valor = dist*0.5 if dist <= 200 else dist*0.45

print(f'Você está prestes a fazer uma viagem de {dist} km.')
print(f'O valor da passagem é de R$ {valor}.')