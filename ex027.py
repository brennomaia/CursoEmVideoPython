n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(nome)
print('Olá, muito prazer em te conhecer!!!')
print('Seu nome é {}'.format(nome[0]))
print('E seu sobrenome é {}'.format(nome[len(nome)-1])) ##  printar o ultimo nome