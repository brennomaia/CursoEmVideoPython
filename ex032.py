#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''from datetime import date
from time import sleep
ano = int(input('Digite o ano para er alisado? 0 é igual o ano atual: '))
print('Vamos analisar o ano de {} é BISEXTO OU NÃO BISEXTO'.format(ano))
sleep(1)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é ano BISSEXTO!!!'.format(ano))
else:
    print('{} não é BISSEXTO'.format(ano))'''
from datetime import date
from calendar import isleap
ano = int(input('Digite o ano para ser analisado, Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print('O {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} não é BISSEXTO'.format(ano))


