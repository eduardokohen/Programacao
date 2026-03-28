#Crie um algoritmo que verifica se um número é ímpar ou par, primo ou não.

from math import sqrt

def eh_primo(num):
    if num < 2:
        return "não é"
    elif num == 2:
        return "é"
    elif num % 2 == 0:
        return "não é"
    else:
        for i in range (3, int(sqrt(num) + 1), 2):
            if num % i == 0:
                return "não é"
    return "é"

def par_ou_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
while True:
    num = int(input('Digite um número ou pressione 0 para sair: '))

    if num == 0:
        print('Encerrando...')
        break
    
    tipo = par_ou_impar(num)
    primo = eh_primo(num)

    print(f'O número {num} é {tipo} e {primo} primo.')