num = int(input("Digite um número: "))

if num >= 0:
    sinal = "positivo"
    if num % 2 == 0:
        condicao = "par"
    else:
        condicao = "ímpar"
else:
    sinal = "negativo"
    if num % 2 == 0:
        condicao = "par"
    else:
        condicao = "ímpar"

print (f"O número {num} é {sinal} e é {condicao}.")