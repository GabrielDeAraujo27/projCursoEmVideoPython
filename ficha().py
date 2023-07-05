def ficha(nome = "none", gols = 0):
    print(f'{nome} fez {gols} gols')


n = input('Qual o nome do jogador? ')
g = input('Quantos gols ele fez? ')
if n == '':
    if g.strip() == '':
        ficha()
    else:
        ficha(gols=g)
else:
    if g.strip() == '':
        ficha(nome=n)
    else:
        ficha(n, g)