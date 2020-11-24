from math import sin, cos, tan, radians
angu = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angu))
cosseno = cos(radians(angu))
tangente = tan(radians(angu))
print('O angulo de {:.1f} tem o SENO de: {:.2f}'.format(angu, seno))
print('O angulo de {:.1f} tem o COSSENO de: {:.2f}'.format(angu, cosseno))
print('O angulo de {:.1f} tem a TANGENTE de: {:.2f}'.format(angu, tangente))