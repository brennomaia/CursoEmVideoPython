
##Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
##e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import choice
from time import sleep
import sys
print('<=>'*32)
print('Vou pensar em um numero de 0 a 5! tente ler a minha mente e acertar o numero em que eu pensei... ')
print('<=>'*32)
lista = [0, 1, 2, 3, 4, 5]
sorteio = choice(lista)### Faz o computador pensar(sortear) um numero da lista
numero = int(input('EAI!! Em qual numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if numero == sorteio:
    print('Parabens! Você leu minha mente!!!')
else:
    print('ERROU!! o numero que eu pensei foi {}'.format(sorteio))
print('----------------- TENTE NOVAMENTE ----------------')

