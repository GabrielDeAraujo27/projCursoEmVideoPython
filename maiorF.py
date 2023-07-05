def maior(list, m):
    for c in range(0, len(list)):
        if list[c] > m:
            m = list[c]
    print(f'O maior número é {m}')


num = []
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? '))
    if r in 'Nn':
        break
r = -99999999999
maior(num, r)