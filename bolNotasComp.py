bolAluno = ['Boletim']
bolAtual = []

cont = 1
while True:
    cont += 1
    bolAtual.append(str(input('Nome: ')))
    bolAtual.append(float(input('Digite a primeira nota: ')))
    bolAtual.append(float(input('Digite a segunda nota: ')))
    bolAtual.append((bolAtual[1]+bolAtual[2])/2)
    bolAluno.append(bolAtual[:])
    bolAtual.clear()
    a = str(input('(S/N)'))
    if a in 'Nn':
        break
print(f'-_-_-_-_{bolAluno[0]}-_-_-_-_')
for c in range(1,cont):
    print(f'{c} - Nome:{bolAluno[c][0]}\nMédia: {bolAluno[c][3]}')
print('-_-_-_-_-_-_-_-_-_-_-_-_')
b = int(input('Qual boletim você deseja saber mais: '))
print(f'Nome: {bolAluno[b][0]}\nNota: {bolAluno[b][1]}\nNota: {bolAluno[b][2]}\nMédia: {bolAluno[b][3]}')