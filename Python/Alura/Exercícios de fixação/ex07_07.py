senha_correta = "py123"
senha = str(input("Digite a senha: "))

while senha != senha_correta:
    print("Senha incorreta!")
    senha = str(input("Tente novamente: "))

print("Acesso liberado!")