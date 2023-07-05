valorCompras=float(input('Quanto você gastou? '))
metPagamento=str(input('Qual será o método de pagamento? '))

if (metPagamento=='dinheiro'):
    pagFinal=valorCompras*0.9
elif (metPagamento=='1x'):
    pagFinal=valorCompras*0.95
elif (metPagamento=='2x'):
    pagFinal=valorCompras
else:
    pagFinal=valorCompras*1.1
print(f'O valor final a ser pago é {pagFinal}')