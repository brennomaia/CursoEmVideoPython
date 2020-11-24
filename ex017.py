from math import hypot
cateOpo = float(input('Digite o valor do cateto oposto: '))
cateAdja = float(input('Digite o valor do cateto Adjacente: '))
print('O comprimento da hipotenusa é {:.2f}'.format(hypot(cateOpo, cateAdja)))