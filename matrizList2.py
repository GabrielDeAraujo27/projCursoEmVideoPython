num = [[],[],[]]

par = soma = maior = 0

for b in range(0,3):
    for c in range(0,3):
        num[b].append(int(input()))

for c in range(0,3):
    print(f'{num[c]}')

for b in range(0,3):
    for c in range(0,3):
        if num[b][c]%2==0:
            par+=num[b][c]

for c in range(0,3):
    soma += num[c][2]

for c in range(0,3):
    if num[2][c]>maior:
        maior = num[2][c]

print(f'A soma dos pares é {par}')
print(f'A soma da terceira coluna é {soma}')
print(f'O maior número da ultima linha é {maior}')