from random import randint
from time import sleep
soma=0
for c in range(0,7):
    R=randint(1,9)
    #R=int(input())
    if (R%2==0):
        soma+=R
        print(R)
    else:
        print('.')
    sleep(0.15)
print(soma)