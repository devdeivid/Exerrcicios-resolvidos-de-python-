#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo, calcule e mostre o
# comprimento da hipotenusa.
from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
ipotenusa = hypot(oposto, adjacente)
print(f'Com os calculos sugeridos digitados {oposto} e {adjacente} a hipotenusa é {ipotenusa:.2f}')