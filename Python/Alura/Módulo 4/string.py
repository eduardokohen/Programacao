palavra = str(input("Digite uma palavra: "))

vogais = 0

for letra in palavra:
    if letra.lower() in "aeiou":
        vogais += 1

print(f"A quantidade de vogais é {vogais}.")