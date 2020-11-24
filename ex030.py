#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


num = int(input('Digite um numero qualquer: '))
calc = num % 2
if calc==1:
    print('O numero {} é IMPAR'.format(num))
if calc==0:
    print('O numero {} é PAR'.format(num))