# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

a = float(input('Digite o primeiro seguimento: '))
b = float(input('Digite o segundo seguimento: '))
c = float(input('Digite o terceiro seguimento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima pode forma um TRIANGULO')
    if a == b == b == c:
        print('EQUILATERO!')

    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISOSCELES')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo')