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

from datetime import datetime
atual = datetime.now().year


titulo = "Bem vindo ao programa de alistamento"
msg = f"Informe sua idade ou um número maior que {atual} para sair"

print(f"{cores['cinza']}-={cores['reset']}"*40)
print(f"{cores['magenta']}{titulo.center(80)}")
print(f"{msg.center(80)}{cores['reset']}")
print(f"{cores['cinza']}-={cores['reset']}"*40)

while True:

    nasc = int(input(f"{cores['azul']}Informe o ano do seu nascimento: {cores['reset']}"))
    minimo = 18

    idade = atual - nasc

    print(f"{cores['verde']}Quem nasceu em {nasc} tem {idade} anos.")

    if idade < 0:
        print(f"{cores['amarelo']}Você está saindo do programa. Até logo!!!{cores['reset']}")
        break
    elif idade >= 0 and idade < minimo:
        print(f"{cores['amarelo']}Ainda não chegou sua vez de se alistar.")
        print(f"Procure o quartel em {nasc + minimo}{cores['reset']}")
    elif idade == minimo:
        print(f"{cores['ciano']}Você tem que se alistar IMEDIATAMENTE!{cores['reset']}")
    else:
        print(f"{cores['vermelho']}Você perdeu sua data de alistamento!")
        print(f"Você devia ter se alistado em {nasc + minimo}!{cores['reset']}")