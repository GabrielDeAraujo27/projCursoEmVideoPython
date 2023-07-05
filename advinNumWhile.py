from random import randint
S=0
N=int(input('Digite o número misterioso: '))
while (S!=N):
    S=randint(1,10)
    print(S)
    if (N==S):
        print('Acertou!')
    else:
        print('Tente novamente.')