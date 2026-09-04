salario = float(input("Digite o seu salário: "))
restricao = str(input("Você possui restrições no CPF? (s/n): ")).lower()
if restricao == "s":
    print("Empréstimo negado devido a restrições no CPF.")
    exit()
tempo = int(input("Há quantos meses você é cliente? "))

if salario >= 3000:
    if tempo >= 24:
        print("Empréstimo aprovado com maior chance de aprovação.")
    else:
        print("Empréstimo aprovado.")
elif salario >= 2000:
    if tempo >= 24:
        print("Empréstimo aprovado.")
    else:
        print("Empréstimo em análise especial.")
else:
    print("Empréstimo negado devido ao salário insuficiente.")