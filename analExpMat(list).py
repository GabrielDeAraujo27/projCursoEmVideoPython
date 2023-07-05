expMat=str(input())
cont1=expMat.count('(')
cont2=expMat.count(')')
if cont2==cont1:
    print('a expressão está certa.')
else:
    print('a expressão está errada.')