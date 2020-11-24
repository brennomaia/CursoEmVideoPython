import random
priAluno = str(input('Digite o nome do primeiro aluno: '))
segAluno = str(input('Digite o nome do segundo aluno: '))
terAluno = str(input('Digite o nome do terceiro aluno: '))
quaAluno = str(input('Digite o nome do quarto aluno: '))
lista = [priAluno, segAluno, terAluno, quaAluno]
sorteio = random.choice(lista)
print('O aluno sorteado parta apagar a louza é: {}'.format(sorteio))