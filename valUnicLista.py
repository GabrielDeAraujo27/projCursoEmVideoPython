unicNum=[]
a=1
while not (a==999):
    a=int(input())
    if a in unicNum:
        break
    else:
        unicNum.append(a)
#unicNum.pop()
unicNum.sort()
print(unicNum)