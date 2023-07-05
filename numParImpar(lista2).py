numPar = []
numImpar = []
listNum = [numPar, numImpar]


for c in range(0,8):
    num = int(input(f'Digite o {c}º número: '))
    if num%2==0:
        numPar.append(num)
    else:
        numImpar.append(num)
    listNum[0].sort()
    listNum[1].sort()
print(f'Você digitou os numeros {listNum}.\nOs números pares são {numPar}\nOs números impares são {numImpar}')
