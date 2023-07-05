nota1=float(input('Qual foi sua nota? '))
nota2=float(input('Qual foi sua nota? '))
nota3=float(input('Qual foi sua nota? '))
nota4=float(input('Qual foi sua nota? '))
media=(nota1+nota2+nota4+nota3)/4

if (media>7):
    print('Aprovado')
elif (media<5):
    print('Reprovado')
elif (media>5) and (media<7) or (media==5):
    print('Recuperação')
else:
    print('Erro')