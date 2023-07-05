idade=int(input('Quantos anos você tem? '))

if (idade==18):
    print('Hora de se alistar')
elif (idade>18):
    print('Já passou da hora de se alistar')
    print('Você devia ter se alistado há', idade-18,'anos')
elif (idade<18):
    print('Ainda não chegou a hora de se alistar')
    print('Você deverá se alistar em', 18-idade, 'anos')