cores = {
    'reset': '\033[0m',
    'preto': '\033[1;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'magenta': '\033[1;35m',
    'ciano':'\033[1;36m'
}

print(f"{cores['amarelo']}-={cores['reset']}" * 30)
print(f"{cores['ciano']}Bem vindo ao comparador numérico!{cores['reset']}".center(60))
print(f"{cores['ciano']}Informe um número ou pressione 0 para sair.{cores['reset']}".center(60))
print(f"{cores['amarelo']}-={cores['reset']}" * 30)

while True:
    
    a = int(input(f"{cores['azul']}Informe o primeiro número: {cores['reset']}"))
    if a == 0:
        print(f"{cores['preto']}Você está saindo do programa. Até logo!!!{cores['reset']}")
        break
    b = int(input(f"{cores['azul']}Informe o segundo número: {cores['reset']}"))
    if b == 0:
        print(f"{cores['preto']}Você está saindo do programa. Até logo!!!{cores['reset']}")
        break
    
    if a > b:
        print(f"{cores['verde']}O primeiro número, {a}, é maior. {cores['reset']}")
    elif a < b:
        print(f"{cores['verde']}O segundo número, {b}, é maior.{cores['reset']}")
    else:
        print(f"{cores['magenta']}Os dois valores {a} e {b} são iguais. {cores['reset']}")
