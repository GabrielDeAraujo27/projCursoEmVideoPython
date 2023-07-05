from random import randint

betNumbers = []
temp = []
betAmount = int(input('Quantas apostas? '))
for c in range(0,betAmount):
    for b in range(0,6):
        temp.append(randint(1,60))
    betNumbers.append(temp[:])
    temp.clear()
print(betNumbers)