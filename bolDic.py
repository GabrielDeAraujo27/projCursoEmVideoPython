boletim = {'nome': '', 'nota': '', 'situação': ''}
boletim['nome'] = input('Nome: ')
boletim['nota'] = int(input('Media: '))

if boletim['nota'] > 6:
    boletim['situação'] = 'Aprovado'
elif boletim['nota'] < 3:
    boletim['situação'] = 'Reprovado'
else:
    boletim['situação'] = 'Recuperação'

for k,v in boletim.items():
    print(f'{k}: {v}')
