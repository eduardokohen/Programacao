#Criando um dicionário de cores

cores = {'limpa':'\033[m',
         'preto':'\033[0;30m',
         'vermelho':'\033[0;31m',
         'verde':'\033[0;32m',
         'amarelo':'\033[0;33m',
         'azul':'\033[0;34m',
         'magenta':'\033[0;35m',
         'ciano':'\033[0;36m',
         'branco':'\033[0;37m'}

reset = cores['limpa']

for cor, codigo in cores.items():
    if cor != 'limpa':
        print(f'Para a cor {codigo}{cor}{reset} o código é {repr(codigo)}')