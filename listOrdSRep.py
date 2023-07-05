list=[]
a=int(input())
list.append(a)
for c in range(1,5):
    a=int(input())
    if (a<list[0]):
        list.insert(0,a)
    elif (a>list[len(list)-1]):
        list.append(a)
    else:
        pos = len(list)
        while (1==1):
            if a>list[pos-1]:
                list.insert(pos, a)
                break
            pos=pos-1
print(list)