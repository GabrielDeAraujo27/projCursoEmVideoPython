from time import sleep
num=int(input('Que tabuada voce quer ver? '))
for c in range(1,11):
    print(f'{num} * {c} = {num*c}')
    sleep(0.25)