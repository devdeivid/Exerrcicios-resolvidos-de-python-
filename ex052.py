#Faça um programa que leia um numero inteiro e diga se ele é ou
# nao um numero primo.
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print('\n\033[mO numero {num} foi divisivel {tot} vezes' )
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso NAO É PRIMO!')
