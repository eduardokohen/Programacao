#criando a tupla:
coordenadas = (10,20)

#atribuir e imprimir os valores da tupla
x,y = coordenadas
print(x,y)

#Tentativa de modificação:
try:
    coordenadas[0] = 99
except:
    print("Você não pode alterar os valores dos itens da tupla!")

#Captura de erro:
try:
    coordenadas[0] = 99
except TypeError as e:
    print("Você não pode alterar os valores de uma tupla!")
    print(e)