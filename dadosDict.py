from random import randint
from operator import itemgetter

dados = {'jogador1':'','jogador2':'', 'jogador3':'', 'jogador4': ''}
dados['jogador1'] = randint(1,6)
dados['jogador2'] = randint(1,6)
dados['jogador3'] = randint(1,6)
dados['jogador4'] = randint(1,6)

for k,v in dados.items():
    print(f'{k} tirou {v}')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
#print(ranking)
for i in range(0,4):
    print(f'{i+1}°posição: {ranking[i]}')

#e = 0
 #   for i in sorted(dados.get):
  #      e += 1
   #     print(f'{e}° lugar: {i} com {dados[i]}')