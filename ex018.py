#Faça um programa que leia um ângulo qualquer e mosttre na tela
# o valor do sena, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angulo = int(input('Digite o ângulo que voce deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem o tangente de {tangente:.2f}')