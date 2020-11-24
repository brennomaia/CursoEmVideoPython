## Exercício Python 037:
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número: '))
binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]
print('ESCOLHA UM DAS BASES PARA CONVERSÃO: \n [ 1 ] converter para BINÁRIO \n [ 2 ] converter para OCTAL \n [ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, binario))

elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(numero, octal))

elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hexadecimal))

else:
    print('Digite uma opção válida')
