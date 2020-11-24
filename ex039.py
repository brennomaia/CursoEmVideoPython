from datetime import date

aNasc = int(input('Digite o ano de nascimento: '))
aAtual = date.today().year
idade = aAtual - aNasc

# Menores de idade
if idade < 18:
    calc = 18-idade
    print('Quem nasceu em {} tem {} anos em {}.\nAinda faltam {} anos para o alistamento militar!\nO alistamento será em {}.'.format(aNasc, idade, aAtual, calc, (aAtual+calc)))

# Maiores
elif idade > 18:
    calc = idade-18
    print('Quem nasceu em {} tem {} anos em {}\nDeveria ter se alistado há {} anos.\nO alismento foi no ano de {}.'.format(aNasc, idade, aAtual, calc, (aAtual-calc)))
# Iguais a 18 anos
elif idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.\nDeve se alistar IMEDIATAMENTE!'.format(aNasc, idade, aAtual))