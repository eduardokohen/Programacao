idade = int(input("Digite a sua idade: "))
if idade < 18:
    print("Você é menor de idade, não pode dirigir!")
    exit()
elif idade >= 18:
    tem_carteira = input("Você tem carteira de motorista? (s/n): ").lower()
    if tem_carteira == "s":
        categoria = input("Qual é a categoria da sua carteira? (A, AB, B, C, D ou E) ").upper()
        if categoria == "A":
            veiculo = "moto"
        elif categoria == "AB":
            veiculo = "moto e carro"
        elif categoria == "B":
            veiculo = "carro"
        elif categoria == "C":
            veiculo = "caminhão"
        elif categoria == "D":
            veiculo = "ônibus"
        else:
            veiculo = "veículo com reboque"
    else:
        print("Você não pode dirigir. Para dirigir você precisa de uma carteira!")
        exit()

print(f"Você tem carteira {categoria}. Você pode dirigir {veiculo}.")