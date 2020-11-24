#salfunc = float(input('O salário do atual funcionario é? '))
#novosal = salfunc + (salfunc*15/100)
#print('O salario com aumento de 15% é R${:.2f}'.format(novosal))

tpedido = float(input('Digite o valor total do pedido: '))
print('O valor total é de R${:.2f}, as condições de pagamento são:\n Á Vista: R${:.2f}\n Parcelado em 2x: R${:.2f}\n Parcelado em 3x: R${:.2f}\n Parcelado em 4x: R${:.2f}\n Parcelado em 5x: R${:.2f}'.format(tpedido, (tpedido-(tpedido*5/100)), ((tpedido+(tpedido*2/100))/2), ((tpedido+(tpedido*3/100))/3), ((tpedido+(tpedido*4/100))/4), ((tpedido+(tpedido*5/100))/5) ))