
'''Manipulando Texto'''

'''Metodos de fatiamento'''
frase = str('Curso em Video Python')
print(frase[9]) ## Mostra o caracter da posição
print(frase[9:14]) ## Mostra os caracters de uma posição até outra posição
print(frase[9:21:2])
print(frase[:15])## Mostra os caracteres do inicio até a posição desejada
print(frase[15:])## Mostra os caracteres da posição até o final da String
print(frase[9::3])
print(frase[::2]) ## Mostra os caracteres do inicio ao vim pulando de dois em doois


''''Metodos para analisar uma string'''
print(len(frase)) #''Mostra o comprimento da frase(Quantidade de caracteres) '''
print(frase.count('o')) #'''Conta a quantidade de um caracter, neste exemplo usei o 'o'''
print(frase.count('o', 0, 13))#'''Conta a quantidade de um caracter até um determinado espaco'''
print(frase.find('o')) # Conta a quantidade de caracteres até o caracter(es) determinado (neste caso utilizamos o caracter o da frase)
print(frase.find('Android')) # -1 significa que essa string não existe ou localizada
print('Curso'in frase)# Analisa se se existe um determinado caracter ou palavra na string (Vardadeiro/Falso)



'''Metodos para transformar uma STRING'''
print(frase.replace('Python', 'Android'))# replace vai subistituir o Python por Android, porem não diretamente na string
print(frase.upper())## Tudo o que esta em caixa baixa tranforma para caixa alta
print(frase.lower())## Tudo em que esta em caixa Alta, transforma para caixa baixa
print(frase.capitalize())## Toda a string em caixa baixa somenta o primeiro caracter em caixa alta
print(frase.title()) ### O primeiro caracter de um palavra em caixa alta


frase1 = str('   Aprenda Python  ')
print(frase1.strip())### Remove os espaços indesejados de uma string
print(frase1.rstrip())### Remove os espaços da Direita mantando os da esquerda
print(frase1.lstrip())###  Remove os espaços da Esquerda


####### Metodos de Divisão de um STRING
print(frase.split())#Divide um String em um lista, separando pelos os espaços
print('-'.join(frase)) ## Gera uma String unica com determinado caracter
