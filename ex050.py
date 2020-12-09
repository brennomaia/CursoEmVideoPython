#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
# EXERCICIO COM BASE DA AULA 13
s = 0 ## Acomulador
for c in range(1, 7):
    num = int(input('Digite o {}º numero: '.format(c)))
    if num % 2 == 0:
        s += num
print('{} é soma de todos os numeros pares'.format(s))