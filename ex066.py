#Crie um programa que leia varios numeros inteiros pelo
# teclado. O programa so vai parar quando o usuario digitar
# o valor 99, que é a condiçao de parada. No final, mostre quantos
# numeros forma digitados e qual foi a soma entre eles
# (desconsiderando o flag).

cont = valor = soma_valores = 0

while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    cont += 1
    soma_valores += valor



print(f'a soma dos {cont} valores foi {soma_valores}!')


