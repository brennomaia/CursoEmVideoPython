#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do colaborador: '))
if salario > 1250.00:
    nsalario = salario + (salario * 10 / 100)

if salario <= 1250:
    nsalario = salario + (salario * 15 / 100)
print('Quem ganhava R${:.2f} passou a ganhar R${:.2f}'.format(salario, nsalario))
