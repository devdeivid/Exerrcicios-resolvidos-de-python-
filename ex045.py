#Crie um programa que faça o computador jogar jokenpo com voce.
from random import randint
from time import sleep
itens = ('PREDA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Suas opçoes:')
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA!!!')
sleep(1)
print('=-'*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-'*20)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('Jogador ganhou!')
    elif jogador == 2:
        print('Computador ganhou!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('Computador Ganhou!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Jogador ganhou!')
    else:
        print('JOGADA INVALIDA!')
if computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador ganhou')
    if jogador == 1:
        print('Computador ganhou!')
    if jogador == 2:
        print('Empatou!')
    else:
        print('JOGADA INVALIDA!')