vproduto = float(input('Qual o valor do produto? '))
calcdesconto = vproduto*5/100
print ('O produto custa R${}, O produto com desconto de 5% vai custarR${}'.format(vproduto, (vproduto-calcdesconto)))