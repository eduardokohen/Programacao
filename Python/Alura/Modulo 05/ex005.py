matriz = [[1, 2],[3,4]]

lista = [v for linha in matriz for v in linha]
print(lista)

lista = []

for linha in matriz:
    for v in linha:
        lista.append(v)

print(lista)