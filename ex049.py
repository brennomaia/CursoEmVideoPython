#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
t = int(input('Digite o valor da tabuada: '))
for c in range(1, 11): ## Contar de 1 a 10
    s = t * c
    print('{} x {} = {}'.format(t, c, s))