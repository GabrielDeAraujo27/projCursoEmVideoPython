maio=0
meno=0
for c in range(0,7):
    idade=int(input())
    if (idade>=18):
        maio+=1
    else:
        meno+=1
print(f'maiores de idade: {maio}. Menores de idade: {meno}.')