#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0  # Acomulador soma
cont = 0 # Acomulador Contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('A soma de todos os {} valores é {}'.format(cont, s))