senha_correta = "py123"
senha = str(input("Digite a senha: "))

while True:
    if senha != senha_correta:
        print("Senha incorreta!")
        senha = str(input("Tente novamente: "))
    else:
        print("Acesso liberado!")
        break