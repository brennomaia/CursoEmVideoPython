valDiaria = float(60)
valKm = float(0.15)
quantDiarias = int(input('Digite a quantidade de diarias: '))
kmPercorrido = float(input('Quantos KMs rodados com o carro? '))
VaTotalDiaria = quantDiarias * valDiaria
VaTotalKm = kmPercorrido * valKm
print('Foram contratados {} dias de aluguel, no total de {}KMs rodados, o valor detalhado do aluguel é de:\n '
      'Valor total de por diarias: R${:.2f}\n '
      'Valor total por KM percorrido: R${:.2f}\n'
      ' Valor total a pagar: R${:.2f}'
      .format(quantDiarias, kmPercorrido, VaTotalDiaria, VaTotalKm, (VaTotalDiaria+VaTotalKm) ))