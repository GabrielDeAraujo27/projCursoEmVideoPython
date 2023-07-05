def leiaInt():
    while True:
        t = input('Digite um numero: ')
        w = t.isnumeric()
        if w == True:
            n = t
            break
    return n



num = leiaInt()

print(f'Você digitou o numero {num}')