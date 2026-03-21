#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
m = int(input('Digite a medida em metros: '))
c = m * 100
mm = m * 1000
print('{} metros equivalem a {} centímetros e a {} milímetros'.format(m, c, mm))
