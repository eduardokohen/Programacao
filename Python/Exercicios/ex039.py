cores = {
    'reset': '\033[0m',
    'cinza': '\033[1;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'magenta': '\033[1;35m',
    'ciano': '\033[1;36m'
}

print(f"{cores['magenta']}-={cores['reset']}"*30)
print(f"{cores['cinza']}Bem vindo ao checador de alistamentos!{cores['reset']}".center(60))
print(f"{cores['magenta']}-={cores['reset']}"*30)

from datetime import datetime

ano_atual = datetime.now().year

while True:

    ano = int(input(f"{cores['verde']}Digite o ano do seu nascimento: {cores['reset']}"))
    minimo = 18
    diferença = ano_atual - ano

    if diferença < minimo and diferença >= 0:
        print(f"{cores['ciano']}Ainda não chegou sua vez!")
        print(f"Seu alistamento será em {ano + minimo}!{cores['reset']}")
    elif diferença == minimo:
        print(f"{cores['amarelo']}Seu alistamento é este ano!")
        print(f"Procure o quartel mais próximo para servir! {cores['reset']}")
    elif diferença > minimo:
        print(f"{cores['vermelho']}Você perdeu a data do alistamento!")
        print(f"Você devia ter se alistado em {ano + minimo}! {cores['reset']}")
    else:
        print(f"{cores['azul']}Entrada inválida!")
        print(f"Informe um ano maior que {ano_atual}!{cores['reset']}")    
        break
