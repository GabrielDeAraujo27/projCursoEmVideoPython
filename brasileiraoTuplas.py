timBR=('FLU', 'FLA', 'CAP', 'BOT', 'RBB', 'COR', 'PAL', 'VAS', 'GRE', 'FOR')

print(f'a) Os 5 primeiros times são: {timBR[0:4]}')

print(f'b) Os últimos 4 colocados: {timBR[6:9]}')

print(f'c) Times em ordem alfabética: {sorted(timBR)}')

print(f'd) Em que posição está o time da Botafogo: {timBR.index("BOT")+1}')