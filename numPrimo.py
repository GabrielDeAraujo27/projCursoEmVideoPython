from time import sleep
P=int(input())
Prim=-1
for c in range(P-1,0,-1):
    if (P%c==0):
        sleep(0.01)
    else:
        Prim+=1
if (Prim==0):
    print(f'O número {P} é primo')
else:
    print(f'O número {P} não é primo')
