#####Exercício Python 029:
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h,mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
from time import sleep
limite = int(50)
velocidade = int(input('Digite a velocidade em que o carro passou no radar: '))
calcmulta = float(velocidade - limite)*7
if velocidade <= limite:
    print('Você está dentro do limite permitido para este trecho da via...')
    print('Boa viagem!!')
else:
    print('ATENÇÃO!!!')
    sleep(2)
    print('Você ultrapassou {}km do limite de 50km/h, E deverá pagar a multa no valor de R${}!!!'.format((velocidade-limite), calcmulta))
    print('Dirija com cuidado!!')
