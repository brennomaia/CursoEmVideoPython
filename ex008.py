## EXECERCICIO 8 - CONVERSOR DE MEDIDAS

medida = int(input('Digite um valor em metros para calcular a distancia: '))
mm = medida*1000
cm = medida*100
dm = medida*10
m = medida
dam = medida/10
hm = medida/100
km = medida/1000

print('O valor de: {} \n Corresponde a : {}mm \n : {}cm \n : {}dm \n : {}m \n : {}dam \n : {}hm \n : {}km '.format((medida), (mm), (cm), (dm), (m), (dam), (hm), (km)))