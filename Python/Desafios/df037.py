nome = str(input('Qual é o seu nome? ')).strip()

if 'Eduardo' in nome.title():
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}'.format(nome.title()))