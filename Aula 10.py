### CONDICOES
### CONDIÇÃO(OES), É DEFINIDA COMO UMA EXPRESSÃO DE VERDADEIRO OU FALSO, ESTA EXPRESSÃO DA O NOME DE EXPRESSÃO RELACIONAL OU COMPARAÇÃO
###  AS ESTRURAS CONDICIONAIS SÃO, SIMPLES, COMPOSTA, ALINHADA, SIMPLIFICADA
### NESTE PROGRAMA UTILIZANDO SOMENTE O "IF" É UMA ESTRUTURA SIMPLES
#### UTILIZANDO "IF E ELSE" É UMA ESTRUTURA COMPOSTA
### QUANDO É UTILIZADO UMA LINHA SÓ É CARACTERIZADA UMA ESTRUTURA CONDICIONAL SOMPLIFICADA

idade = int(input('Digite quantos anos você tem: '))
if idade <18:
    print('PARE! Você não tem idade suficiente!')
else:
    print('Parabens, Você é maior de idade!')
print('FIM DO PROGRAMA...')

print('Você é menor'if idade<18 else'Você é maior')




############### SEGUNDO TESTE /// CALCULANDO A MEDIA DO SEMESTRE UNIP


av1 = float(input('Digite sua nota da Primeira Avaliação: '))
av2 = float(input('Digite sua nota da Segunda Avaliação: '))
pim = float(input('Digite o valor do seu PIM: '))

media = ((av1 + av2)+(pim*30/100))/2
print('Sua média do semestre foi {}'.format(media))
if media < 6.0:
    print('Estude mais! Você foi REPROVADO!')
else:
    print('PARABENS! Você foi APROVADO!!')