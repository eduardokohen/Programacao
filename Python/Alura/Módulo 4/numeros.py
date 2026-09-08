numeros = [1,2,3,4,5,6,7,8,9,10]

print("Utilizando o BREAK: ")
for i in numeros:
    if i % 2 == 0:
        print(f"Cheguei no {i}. Encerrando o laço")
        break

print("Utilizando o CONTINUE: ")
for i in numeros:
    if i % 2 == 0:
        print(f"Cheguei no {i}. Pulando para o próximo par.")
        continue