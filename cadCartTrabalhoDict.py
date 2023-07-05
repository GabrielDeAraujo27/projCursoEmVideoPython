cartTrab = {'nome': '', 'idade': '', 'CTPS': '', 'Contratação': '', 'Salário': '', 'Aposentadoria': ''}

cartTrab['nome'] = str(input('Nome:'))
cartTrab['idade'] = 2023 - int(input('Data de Nascimento: '))
cartTrab['CTPS'] = int(input('Número da Carteira de Trabalho: '))

if cartTrab['CTPS']>0:
    cartTrab['Contratação'] = int(input('Ano de Contratação: '))
    cartTrab['Salário'] = float(input('Salário: '))
    cartTrab['Aposentadoria'] = int(input('ano de Aposentadoria: ')) - (2023-cartTrab['idade'])

print(f"O nome é {cartTrab['nome']}\n"
      f"A idade de {cartTrab['nome']} é {cartTrab['idade']}\n"
      f"O número da carteira de trabalho de {cartTrab['nome']} é {cartTrab['CTPS']}")
if cartTrab['CTPS']>0:
    print(f"{cartTrab['nome']} foi contratado em {cartTrab['Contratação']}\n"
          f"{cartTrab['nome']} recebe R${cartTrab['Salário']} por mês\n"
          f"{cartTrab['nome']} se aposentará com {cartTrab['Aposentadoria']}")