def voto():
    global i
    global a
    if i > 60:
        a = "opcional"
    elif i < 18:
        a = "negado"
    else:
        a = "obrigatório"

a = '0'
n = str(input('Qual o seu nome? '))
i = int(input('Qual a sua idade? '))
voto()
print(f'{a}')