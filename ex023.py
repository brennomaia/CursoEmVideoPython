num = int(input('Insira um numero: '))
print('Analisando o numero {} ...'.format(num))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Desena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
