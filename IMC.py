peso=float(input('Quanto você pesa? '))
altura=float(input('Quanto você mede? '))

IMC=peso/(altura*altura)
print(f'{IMC:,.2f}')

if (IMC<18.5):
    print(f'O IMC {IMC:,.2f} está abaixo do ideal')
elif (IMC>18.4) and (IMC<25):
    print(f'O IMC {IMC:,.2f} está no peso ideal')
elif (IMC>24.9) and (IMC<30):
    print(f'O IMC {IMC:,.2f} está com sobrepeso')
elif (IMC>29.9) and (IMC<40):
    print(f'O IMC {IMC:,.2f} está com obesidade')
elif (IMC>39.9):
    print(f'O IMC {IMC:,.2f} está com obesidade mórbida')