# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint #RANDOMIZANDO EMBARALHANDO
from time import sleep

print(' VAMOS JOGAR JOKENPO ')
itens = ('pedra', 'papel', 'tesoura')### 3 STRINGS, POSIÇÃO 0, 1 e 2
computador = randint(0, 2) # O COMPUTADOR VAI ESCOLHER(SORTEAR) UM NUMERO ENTRE 0 E 2

jogador = int(input('''O que você vai escolher?
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA
Digite sua opção:'''))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

############# COMPARANDO AS JOGADAS ###################
print('<=>' * 10)
print('O computador escolheu {}!'.format(itens[computador])) # O COMPUTADOR VAI ESCOLHER UM ITEM DE ACORDO COM A POSIÇÃO (0, 1 E 2)
print('O jogador escolheu {}!'.format(itens[jogador])) # O JOGADOR ESCOLHE O INTEM DE ACORDO COM A POSIÇÃO
print('<=>' * 10)


########## DEFINIANDO UM GANHADOR ################
if computador == 0 :#O COMPUTADOR ESCOLHEU PEDRA
    if jogador == 0:
        print('EMPATE')
    if jogador == 1:
        print('O jogador GANHOU')
    if jogador == 2:
        print('O computador GANHOU')

elif computador == 1: #O COMPUTADOR ESCOLHEU PAPEL
    if jogador == 0:
        print('O computador GANHOU')
    if jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print('O jogador GANHOU')

elif computador == 2: #O COMPUTADOR ESCOLHEU TESOURA
    if jogador == 0:
        print('O jogador GANHOU')
    if jogador == 1:
        print('O computador GANHOU')
    if jogador == 2:
        print('EMPATE')