from time import sleep

fNum=float(input('Primeiro número: '))
sNum=float(input('Segundo número: '))
opc=4

while (opc!=5):
    opc=int(input(f'[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n'))
    if (opc==1):
        print(f'O resultado da soma dos números {fNum} e {sNum} é {fNum+sNum}.')
    elif (opc==2):
        print(f'O resultado da multiplicação dos números {fNum} e {sNum} é {fNum*sNum}.')
    elif (opc==3):
        if (fNum>sNum):
            print(f'O maior número entre {fNum} e {sNum} é {fNum}.')
        else:
            print(f'O maior número entre {fNum} e {sNum} é {sNum}.')
    elif (opc==4):
        fNum = float(input('Primeiro número: '))
        sNum = float(input('Segundo número: '))
    sleep(0.25)