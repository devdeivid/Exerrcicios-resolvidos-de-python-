#Melhore o jogo do desafio 028 onde o computador vai 'pensar'em um numero
# entre 0 e 10. Só que agora o Jogador vai tenta adivinhar até acertar,
# mostrando no final quantos palpites foram necessarios para vencer.
from random import randint
from time import sleep
computador = randint(1,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que voce consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qualo é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez. ')
        elif jogador > computador:
            print('Menos.... tante mais uma vez.')
print(f'Acertou com {palpites} tentaticas. Parabéns!')