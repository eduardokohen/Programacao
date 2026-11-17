peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))

imc = peso/(altura ** 2)

if imc < 18.5:
    situacao = "abaixo do peso"
elif imc <= 25:
    situacao = "com peso ideal"
elif imc <= 30:
    situacao = "com sobrepeso"
elif imc <= 40:
    situacao = "com obesidade"
else:
    situacao = "com obesidade mórbida"

print(f"O seu IMC é de {imc:.2f}. Você está {situacao}!")