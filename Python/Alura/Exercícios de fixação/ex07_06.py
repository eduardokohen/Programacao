senha_correta = input("Digite a senha: ")
senha = "py123"

while senha != senha_correta:
    print("Senha incorreta!")
    senha = input("Tente novamente: ")

print("Acesso liberado!")