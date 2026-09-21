senha_correta = "py123"
senha = input("Digite sua senha: ")

while senha != senha_correta:
    print("Senha incorreta!")
    senha = input("Tente novamente: ")

print("Acesso liberado!")