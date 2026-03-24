#Faça um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias que ele foi alugado
#Calcule o preço a pagar sabendo que o carro custa R$60/dia + R$0.15/km

d = int(input('Informe a quantidade de dias que o carro foi alugado: '))
km = float(input('Informe a quantidade de quilômetros rodados: '))

vd = d*60
vkm = km*0.15
vt = vd + vkm

print('O carro esteve alugado por {} dias e rodou {:.2f} km. O valor a ser pago é de {:.2f}'.format(d, km, vt))