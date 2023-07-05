from time import sleep
while True:
    num=int(input('Que tabuada voce quer ver? '))
    if (num<0):
        break
    cont=0
    print('------------------')
    while (cont<10):
        cont+=1
        print(f'{num} * {cont} = {num*cont}')
        sleep(0.25)