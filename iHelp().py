def iHelp(a='help'):
    print(f'\n\n\n')
    help(a)

while True:
    r = input('Digite o comando que você tem dúvida: ')
    iHelp(r)
    r = input('Quer continuar? ')
    if r in 'Naonao':
        break