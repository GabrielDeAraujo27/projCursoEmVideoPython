def contador(inicio, fim, passo):
    for c in range(inicio, (fim+passo), passo):
        print(f'{c}...')


x = int(input('Qual o número inicial da contagem? '))
y = int(input('Qual o número final da contagem? '))
z = int(input('Qual o passo da contagem? '))
contador(x, y, z)