## AULA 13 --- ESTRUTURA DE REPETIÇÃO "FOR"
#Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o "for".
# que é uma estrutura versátil e simples de entender. Por exemplo:


print('##EXEMPLO##')
for c in range(0, 10): ### CONTANDO DE 0 A 10
     print(c)
print('Acabou')

for c in range(0, 10, 2): ### CONTANDO DE 0 A 10 "PULANDO DE 2 EM 2"
     print(c)
print('Acabou')

n = int(input('Digite um número: ')) ## Pedindo um numero
for c in range(0, n+1):   ### contando de 0 ao numero pedido
     print(c)


### SOMATORIA TOTAL DOS NUMEROS SOLICITADOS
s = 0 ### Usando o "s" como acomulador.
for c in range(0, 4):  ### Quantidade de repetições
     n = int(input('Digite um valor: '))
     s += n ### somatoria do numeros pedidos e anexados da variavel n
print('O somatorio de todos os valores é {}'.format(s))