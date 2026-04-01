nome = str(input('Qual é o seu nome? '))

if nome == 'Eduardo' or nome == 'Estêvão':
    print('Seu Nome é muito bonito.')

elif nome == 'João' or nome == 'José' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')

elif nome in 'Izabela Sofia Helena Mariana':
    print('Belo nome feminino.')

print('Tenha um bom dia, {}!'.format(nome))