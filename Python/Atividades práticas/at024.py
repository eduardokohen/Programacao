while True:
    num = int(input("Digite um número inteiro maior que 1: "))

    if num <= 1:
        print("Número inválido! Digite um número inteiro maior que 1.")
    else:
        break  # sai do laço quando o número for válido

# A partir daqui, sabemos que num > 1

if num % 2 == 0:
    print(f"O número {num} é par")
else:
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(f"O número {num} é ímpar e é primo")
    else:
        print(f"O número {num} é ímpar")