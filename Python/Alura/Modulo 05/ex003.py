#Use uma compreensão de lista para criar uma lista de quadrados
#A lista deve conter os quadrados dos números de 0 a 4 (use range(5))
#Imprima a lista resultante.
#Escreva seu código aqui:

lista = []

for i in range(5):
    lista.append(i**2)
print(lista)

#De outra forma:

lista_2 = [x**2 for x in range(5)]
print(lista_2)