#Crie um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem cobrando R$0,50 por km para viagens de até 200km.
#Se a viagem for maior que 200km, calcule o preço da passagem cobrando R$0.45/km

distancia = float(input('Informe a distância da viagem: '))

if distancia <= 200:
    preço = 0.50 * distancia
    print('O valor da passagem é de {:.2f} reais.'.format(preço))

else:
    preço = 0.45 * distancia
    print('O valor da passagem é de {:.2f} reais.'.format(preço))