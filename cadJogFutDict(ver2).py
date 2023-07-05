time = []
player = {"nome": "", "numJog": "", "totalPont": 0, "pontJ": ""}
pont = []
t = 0
time.append(t)
while True:
    player["pontJ"] = pont
    player["nome"] = str(input('Nome do Jogador: '))
    player["numJog"] = int(input('Quantos jogos ele jogou nessa temporada? '))
    for c in range(0,player["numJog"]):
        pont.append(int(input(f'Quantos pontos {player["nome"]} fez no jogo {c+1}: ')))
        player["totalPont"] += pont[c]
        t += pont[c]
    time.append(player.copy())
    r = input('Quer continuar cadastrando jogadores? ')
    if r in 'nN':
        break
r = input('Que jogador você quer saber os dados? ')
print(f"O jogador {time[r]['nome']} fez {time[r]['totalPont']} pontos no total"
      f'O time fez {time[0]} gols no total')