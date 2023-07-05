from random import randint
listNum=[]
for c in range(0,randint(3,9)):
    listNum.append(int(input()))
listNum.sort(reverse=True)
if 5 in listNum:
    p5=listNum.index(5)
    P=True
print(f'{len(listNum)}')
print(f'{listNum}')
if (P==True):
    print(f'Na posição {p5}')

#print(listNum)