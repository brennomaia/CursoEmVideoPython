largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
dimensao = largura*altura
tinta = dimensao/2
print('Sua parede possui a dimensão de {}x{} e sua area é de {}m²\n Para pintar está parede você precisa de {}l de tinta'.format(largura, altura, dimensao, tinta))