#Faça um programa que leia um numero qualquer e mostre seu
# factorial.
#ex: 5! = 5x4x3x2x1 = 120
from math import factorial
n1 = (int(input('Digite um numero: ')))
n2 = factorial(n1)
print(f'O factorial de {n1} é {n2}. ')