#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuario venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0, 5)
print('--=' * 30)
print(' Vou pensar em um numero entre 0 e 5. tente adivinhar... ')
print('--=' * 30)
n1 = int(input('Em Qual numero eu pensei? '))
print('PROCESSANDO... ')
sleep(2)
if n1 == computador:
    print(f'PARABÉNS! Você conseguiu me vencer! ')
else:
    print(f'Ganhei! Eu pensei no numero {computador} e nao no {n1}')


