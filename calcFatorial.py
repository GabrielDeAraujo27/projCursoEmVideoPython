num=int(input('Digite o número: '))
numIni=num
cont=num
while (cont!=1):
    cont-=1
    num=num*cont
    print(cont)
print(f'O fatorial de {numIni} é {num}.')