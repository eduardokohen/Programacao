cidade = str(input('Em qual cidade você nasceu? ')).strip()

cidade = cidade.upper()

tem_santo = 'SANTO' in cidade

print(tem_santo)