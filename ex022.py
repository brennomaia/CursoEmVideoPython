
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome completo em letras maiúsculas nome.upper {}'.format(nome.upper()))
print('Seu nome completo em letras minúsculas {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find('lo')))
separa = nome.split()
print('Seu primeiro nome é {} ele tem ao todo {} letras'.format(separa[0], len(separa[0]))