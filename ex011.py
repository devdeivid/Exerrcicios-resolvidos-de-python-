#Faça um programa que leia a largura e a alatura de uma parede
#em metros, calcule a sua area e a quantidade de tinta nescessaria
# para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m².
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimençao de {largura:.2f}x{altura:.2f} e sua area é de {area:.1f}m²')
tinta = area / 2
print(f'Sua parede vai precisar de {tinta:.1f} litros de tinta')