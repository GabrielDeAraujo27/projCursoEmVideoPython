maior=float(-1)
menor=float(1000)
for c in range(0,5):
    num=float(input())
    if (num>maior):
        maior=num
    if (num<maior):
        menor=num
print(f'O maior número é {maior}. O menor número é {menor}.')