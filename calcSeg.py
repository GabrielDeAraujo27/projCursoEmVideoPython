from time import sleep

contPontFin = int(1)
print('Iniciado....', end='')

while (contPontFin > 0):
    sleep(0.75)
    print('..', end='')
    contPontFin = contPontFin - 0.20

print('..')

priNum = int(input('Digite o primeiro número: '))
segNum = int(input('Digite o segundo número: '))

opMat = str(input ('Que operação você deseja efetuar? '))

if (priNum==78) and (segNum==194):
    secr = bool (True)
    #aaaaaaaaaaaaaaaa

if (opMat == '+'):
    resOp = priNum + segNum
elif (opMat == '-'):
    resOp = priNum - segNum
elif (opMat == '*'):
    resOp = priNum * segNum
elif (opMat == '/'):
    resOp = priNum / segNum
elif (opMat == '^'):
    resOp = pow(priNum, segNum)
else:
    print('Comando inválido')
    exit()

print (priNum, opMat, segNum, '=', resOp)
if (secr==True):
    print('A verdade é que o maior motivo pra você rir de pessoas pequenas é cobiça. Você vive')
    print('uma vida incompleta pois sabe que nunca encontrará uma mulher com pelo menos 30 cm ')
    print('a mais de altura do que você.')