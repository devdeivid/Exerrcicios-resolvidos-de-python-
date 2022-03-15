#Escreva um programa que leia um numero inteiro qualquer e peça para o
# usuario escolher qual será a base de converçao:
#- 1 para binario
#- 2 para octal
#- 3 para hexadecimal

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('Sua opçao: '))
if opçao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)}')
elif opçao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)}')
elif opçao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print('Opçao invalida. Tente novamente.')

