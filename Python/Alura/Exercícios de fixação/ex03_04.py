num = int(input("Digite um número inteiro: "))

if num >= 0:
    if num % 2 == 0:
        print(f"O número {num} é positivo e é par.")
    else:
        print(f"O número {num} é positivo e é ímpar.")
else:
    if num % 2 == 0:
        print(f"O número {num} é negativo e é par.")
    else:
        print(f"O número {num} é negativo e é ímpar.")