#Escreva um programa que leia um número em metros e o exiba convertido em centímetros e milímetros

n = int(input('Digite um número: '))
cm = n*100
mm = n*1000

print('A medida em metros é {} \nA medida em centímetros é {} \nA medida em milímetros é {}' .format(n, cm, mm))