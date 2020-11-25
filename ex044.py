#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
'''

produto = float(input('Digite o valor do produto: R$ '))
print('\n [ 1 ] À vista em dinheiro/cheque com 10% de Desconto.'
      '\n [ 2 ] À vista no cartão débito/crédito com 5% de desconto.'
      '\n [ 3 ] Parcelado em até 2x sem juros.'
      '\n [ 4 ] 3 x ou mais com juros de 20% no total do produto.')
pagamento = int(input('Escolha a forma de pagamento: '))

if pagamento == 1:
    print('Pagamento no valor de R${:.2f}\nCom 10% de desconto!'.format(produto - (produto * 10 / 100)))

elif pagamento == 2:
    print('Pagamento no valor de R${:.2f}\nCom 5% de desconto!'.format(produto - (produto * 5 / 100)))

elif pagamento == 3:
    print('Pagamento no valor de R${:.2f}\nParcelado em 2x!'.format(produto))

elif pagamento == 4:
    print('Pagamento no valor de R${}\nCom acréscimo de 20%!'.format(produto + (produto * 20 / 100)))
'''


##### APÓS VER O VIDEO ####
produto = float(input('Digite o valor do pedido: R$ '))
print('\n [ 1 ] À vista em dinheiro/cheque com 10% de Desconto.'
      '\n [ 2 ] À vista no cartão débito/crédito com 5% de desconto.'
      '\n [ 3 ] Parcelado em até 2x sem juros.'
      '\n [ 4 ] 3 x ou mais com juros de 20% no total do produto.')
pagamento = int(input('Escolha a forma de pagamento: '))

if pagamento == 1:
    print('Pagamento no valor de R${:.2f}\nCom 10% de desconto!'.format(produto - (produto * 10 / 100)))

elif pagamento == 2:
    print('Pagamento no valor de R${:.2f}\nCom 5% de desconto!'.format(produto - (produto * 5 / 100)))

elif pagamento == 3:
    print('Pagamento no valor de R${:.2f}\nParcelado em 2x!'.format(produto))

elif pagamento == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    print('Pagamento em {}x no valor de R${:.2f} no total de R${:.2f}\nCom acréscimo de 20%!'.format(parcelas, ((produto+(produto*20/100))/parcelas), produto + (produto * 20 / 100)))
