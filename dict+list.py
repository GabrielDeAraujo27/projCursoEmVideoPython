sistCad = []
mulh = []
cad = {"nome": '', "sexo": '', "idade": int(0.0)}

total = media = num = maiQMedia = 0

for c in range(1,99999999):
    cad["nome"] = input(f'Qual o nome do funcionário {c}? ')
    cad["sexo"] = input(f'E o sexo? ')
    if cad["sexo"] in 'fF':
        mulh.append(cad["sexo"])
    cad["idade"] = input(f'E a idade? ')
    r = input('Deseja continuar? ')
    sistCad.append(cad.copy())
    if r in 'NnNaoNãonaonão':
        break
for c in range(0,len(sistCad)):
    total += int(sistCad[c]['idade'])
    #total = total + num
media = float(total / c)
for c in range(0,len(sistCad)):
    if int(sistCad[c]['idade']) > media:
        maiQMedia += 1
print(f'{len(sistCad)} pessoas foram cadastradas.\n'
      f'{maiQMedia} pessoas estão acima da média de idade\n'
      f'{mulh} foram as mulheres cadastradas')