def fatorial(n, s):
    for c in range(n-1, 0, -1):
        if s in 'Ssim':
            print(f'{c}!', end=' ')
            if c > 1:
                print(f'* ', end='')
        n *= c
    return n


num = int(input('Digite um número: '))
show = str(input('Quer ver o processo? '))
print(f'{num}! ', end='')
if show in 'Ssim':
    print(f'* ', end='')
r = fatorial(num, show)
print(f'= {r}')