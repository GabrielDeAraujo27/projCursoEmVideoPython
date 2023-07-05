numInic=int(input('Digite um número: '))
basenum=int(input('Pra qual base numérica você deseja converter esse número? '))

if (basenum==2):
    numFim=str(bin(numInic))
elif (basenum==8):
    numFim=str(oct(numInic))
elif (basenum==16):
    numFim=str(hex(numInic))
else:
    print('Você digitou o número errado')

print(numFim[2::])