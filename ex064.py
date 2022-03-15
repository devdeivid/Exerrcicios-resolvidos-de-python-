#Crie um programa que leia varios numeros inteiros pelo teclado.O programa so vai parar
# quando o usuario digitar o valor 999, que é a condiçao de parada.No final, mostre quantos
# numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag).
n1 = cont = soma = 0
n1 = int(input('Digite um numero: [999 para parar]: '))
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input('Digite um numero[99 para parar]: '))

print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}')



