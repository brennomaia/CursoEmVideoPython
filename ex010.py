carteira = float(input('Digite quanto você tem sua carteira: R$'))
us = 5.59
eur = 6.57
print('Com R${} você pode comprar\n ${:.2f}\n €{:.2f}'.format(carteira, (carteira/us), (carteira/eur)))
