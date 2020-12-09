#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
# EXERCICIO COM BASE DA AULA 13


s = 0  # Acomulador soma
cont = 0 # Acomulador Contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # A quantidade de numero multiplos de 3
        s += c # a soma de todos os valores
print('A soma de todos os {} valores é {}'.format(cont, s))