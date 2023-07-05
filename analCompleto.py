medIdade=0
nomHomMaisVelho='Indefinido'
idadHomMaisVelho=0
numMulhJovens=0
for c in range(0,4):
    nome=input('Nome: ')
    sexo=input('Sexo: ')
    idade=int(input('Idade: '))
    medIdade += idade
    if (sexo=='F'):
        if (idade<=20):
            numMulhJovens+=1
    elif (sexo=='M'):
        if (idade>idadHomMaisVelho):
            idadHomMaisVelho=idade
            nomHomMaisVelho=nome
    else:
        exit()
medIdade=(medIdade/c)
print(f'A média de de idade é {medIdade}.\nO nome do homem mais velho é {nomHomMaisVelho} com notáveis {idadHomMaisVelho}.')
print(f'Existem {numMulhJovens} mulheres com menos de 20 anos.')