#Faça um programa que leia a largura e a altura de uma parede, em metros, calcule a sua área  e a quantidade de tinta necessária para pintá-la, sabendo que cada litros de tinta, pinta uma área de 2m2.
al = float(input('Qual a altura da parede em metros?: '))
lar = float(input('Qual a largura da parede em metros?: '))
área = al * lar
print('Se sua parede tem {}x{}, a área dessa parede é igual a {} metros quadrados.'.format(al, lar, área))
print('Quantos litros de tinta são necessários para pintar a parede toda? \n-----Considerando que 1 litro pinta 2m2-----')
parede_toda = área / 2
print('Serão necessários {} litros de tinta.'.format(parede_toda))
print('')
print('aperte ENTER para sair')

# ok
