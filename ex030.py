#Crie um programa que leia um numero inteiro e mostre na
#tela se ele é PAR ou Impar.
num = int(input('Digite um nomero: '))
resultado = num % 2
if resultado == 0:
    print(f'Esse numero é PAR! ')
else:
    print('Esse numero é IMPAR! ')