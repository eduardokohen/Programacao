idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Você é menor de idade, não pode dirigir!")
    exit()

tem_carteira = input("Você tem carteira de motorista? (s/n): ").lower()

if idade >= 18:
    if tem_carteira == "s":
        print("Você pode dirigir!")
    else:
        print("Você não pode dirigir.")