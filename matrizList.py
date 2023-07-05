num = ['P']


for c in range(1,10):
    num.append(int(input()))
for c in range(1,10):
    print(f'{num[c]}', end='     ')
    if c%3==0:
        print(f'\n')