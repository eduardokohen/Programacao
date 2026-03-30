#Testando todas as cores em python:

reset = '\033[m'

for cor in range(30,38):
    for back in range(40,48):
        print(f'\033[1;{cor};{back}mOlá Mundo!{reset}')
        print(f'A cor é {cor} e o background é {back}')