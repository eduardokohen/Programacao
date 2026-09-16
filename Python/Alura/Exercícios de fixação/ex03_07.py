num = int(input("Digite um número: "))

if num >= 0:
    sinal = "positivo"
else:
    sinal = "negativo"
if num % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

print(f"O número {num} é {sinal} e é {paridade}.")