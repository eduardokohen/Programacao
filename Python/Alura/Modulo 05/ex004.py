lista = []

for i in range(6):
    num = int(input(f"Digite o {i+1}º termo da lista: "))
    lista.append(num)

lista_2 = [x**2 for x in range(5)if x > 0]

print(lista)
print(lista_2)