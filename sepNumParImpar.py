num=[]
numImpar=[]
numPar=[]

for c in range (0,5):
    a=int(input())
    num.append(a)
for c in range (0,5):
    if (num[c - 1]%2==0):
        numPar.append(num[c - 1])
    else:
        numImpar.append(num[c - 1])
print(f'{num}\n{numPar}\n{numImpar}')