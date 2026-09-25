valores = range(1,11)

for numero in valores:
    if numero == 7:
        print("Parando aqui...")
        break
    multiplicacao = numero * 5
    print(f"O produto de {numero} x 5 é: {multiplicacao}.")