##Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vCasa = float(input('Digite o valor da casa: R$'))
salComprador = float(input('Digite o salário do comprador: R$'))
periodo = int(input('Digite quantos anos será o financiamento?'))
calcSalario = float(salComprador * 30 / 100)
vParcela = float(vCasa / (periodo * 12))

print('O financimento do imóvel no valor de R${:.2f} em {}x, a parcela será de R${:.2f}.'.format(vCasa, (periodo*12), vParcela))

if vParcela < calcSalario:
    print('O seu empréstimo foi APROVADO')
else:
    print('O seu empréstimo NEGADO')
