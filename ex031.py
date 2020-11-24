#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distancia da sia viagem: '))
print('A sua viagem de {}.km irá começar.'.format(distancia))
if distancia <= 200:
    print('O valor da viagem é de: R${:.2f}'.format(distancia*0.50))
else:
    distancia > 200
    print('O valor da viagem é de: R${:.2f}'.format(distancia*0.45))