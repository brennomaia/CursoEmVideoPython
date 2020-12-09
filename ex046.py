## Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.


soma = 0 ### Acomulador de soma
cont = 0 #### acomulador de contagem
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 ### Contagem de numero diviseis por 3
        soma += c ### Soma de todos os valores diviseis por 3

print('A soma de todos os {} valores é {}'.format(cont, soma))