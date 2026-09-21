senha = str(input("Digite a senha: "))
senha_correta = "py123"

while senha != senha_correta:
    print("Senha incorreta!")
    senha = str(input("Tente novamente: "))

print("Acesso liberado!")