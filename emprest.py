salario=int(input("Qual o valor de seu salário?"))
casa=int(input("Qual o valor da casa que você planeja comprar?"))
numPrestacao=int(input("Por quantos anos você planeja pagar as prestações?"))
valorPrestacao=casa/(numPrestacao*12)

if (valorPrestacao<salario*0.3):
    print("Infelizmente, não será possivel prosseguir com o emprestimo")
elif (valorPrestacao==salario*0.3):
    print("Felizmente você conseguirá prosseguir com o emprestimo")
else:
    print("Parabéns, vamos prosseguir com o emprestimo")






