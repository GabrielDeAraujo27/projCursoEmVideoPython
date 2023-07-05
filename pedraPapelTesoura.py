from random import randint
from time import sleep
winner=str('0')
while (winner=='0'):
    print(f'-------------------------------\n1 - Pedra \n2 - Tesoura \n3 - Papel')
    play=str(input('Qual a sua jogada? '))
    if (play=='1'):
        playF='pedra'
    elif (play=='2'):
        playF='tesoura'
    elif (play=='3'):
        playF='papel'

    print(f'A jogada do player foi {playF}.')
    sleep(1)

    bot=randint(1,3)
    if (bot==1):
        botF='pedra'
    elif (bot==2):
        botF='tesoura'
    elif (bot==3):
        botF='papel'

    print(f'A jogada do bot foi {botF}.')
    sleep(1)

    if (playF=='pedra'):
        if (botF=='tesoura'):
            winner='Player'
        elif (botF=='papel'):
            winner="Bot"
        else:
            print('Empate. Tente novamente.')
    if (playF=='tesoura'):
        if (botF=='papel'):
            winner='Player'
        elif (botF=='pedra'):
            winner="Bot"
        else:
            print('Empate. Tente novamente.')
    if (playF=='papel'):
        if (botF=='pedra'):
            winner='Player'
        elif (botF=='tesoura'):
            winner="Bot"
        else:
            print('Empate. Tente novamente.')
    sleep(1.5)

print(f'O ganhador foi o {winner}.')