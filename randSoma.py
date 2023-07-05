from random import randint
def sorteia(ale):
    for c in range(0,5):
        ale.append(randint(0,9))
def somaPar(list, t):
    for c in range(0,len(list)):
        if list[c]%2==0:
            t += list[c]
    print(f'A soma dos pares é {t}')
num = []
total = 0
sorteia(num)
print(sorted(num))
somaPar(num, total)
