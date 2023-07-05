pesIdaPeso=[]
lisPesIdaPeso=[]

maiorPeso=0.0
maisPesado = '/'
menorPeso=9999999999999999.0
menosPesado= '/'
for c in range (0,3):
    pesIdaPeso.append(str(input('Digite o nome: ')))
    pesIdaPeso.append(int(input('Digite a idade: ')))
    pesIdaPeso.append(float(input('Digite o peso: ')))

    if pesIdaPeso[2]>maiorPeso:
        maiorPeso=pesIdaPeso[2]
        maisPesado=pesIdaPeso[0]
    if pesIdaPeso[2]<menorPeso:
        menorPeso=pesIdaPeso[2]
        menosPesado=pesIdaPeso[0]
    lisPesIdaPeso.append(pesIdaPeso[:])
    pesIdaPeso.clear()
print(f'Foram cadastradas {len(lisPesIdaPeso)} pessoas.')
print(f'O menor peso foi de {menosPesado} e o maior peso foi de {maisPesado}.')
