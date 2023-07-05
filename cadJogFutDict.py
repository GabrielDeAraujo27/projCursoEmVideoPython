player = {"nome": "", "numJog": "", "totalPont": 0, "pontJ": ""}
pont = []
player["pontJ"] = pont
player["nome"] = str(input('Nome do Jogador: '))
player["numJog"] = int(input('Quantos jogos ele jogou nessa temporada? '))
for c in range(0,player["numJog"]):
    pont.append(int(input(f'Quantos pontos {player["nome"]} fez no jogo {c+1}: ')))
    player["totalPont"] += pont[c]
print(f'O jogador {player["nome"]} fez {player["totalPont"]} pontos no total')