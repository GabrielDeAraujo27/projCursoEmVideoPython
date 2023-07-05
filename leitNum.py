cont=0
while True:
    numAtual=int(input('Digite um número: '))
    if (numAtual==999):
        break
    else:
        cont+=1
print(f'Você digitou {cont} números')