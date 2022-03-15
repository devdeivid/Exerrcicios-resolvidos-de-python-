'''1 - Crie um funçao que exibe uma saudaçao com os parâmetros saudaçao e nome.'''
'''def saudaçao (saudaçao, nome):
    print(f'{saudaçao}{nome}')

saudaçao('Olá', ' Joaozinho')
saudaçao('Oi', ' Maria')
saudaçao('Hey', ' Aline')'''
""" 2 - Crie funçao que recebe 3 numeros como parâmetros e exiba a soma entre eles."""
'''def soma (n1, n2, n3):
    print(n1 + n2 + n3)
soma(3, 5, 7)
soma(8, 2, 4)
soma(9, 3, 1)
soma(3, 4, 1)
soma(8, 3, 1)
soma(9, 3, 4)'''
#3 - Crie uma funçao que receba 2 numeros. O primeiro é um valor e o segundo um percentual
# (ex. 10%). Retorne(return) o valor do primeiro numero somado do aumento do percentual do
# mesmo.
'''def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual / 100))

aumento_percentual(50, 1000)
aumento_percentual(100, 90)
aumento_percentual(10, 10)
aumento_percentual(15, 100)
'''
#4 - Fizz Buzz - Se o parametro da funçao for divisivel por 3,
# retorne fizz, se o parÂmetro da funçao for divisivel por 5,
# retorne buzz. Se o parâmetro da funçao for divisivel por 5 e
# por 3, retorne FizzBuzz, caso contrario, retorne o numero enviado.


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisivel por 3 por 5'
    if n % 5 == 0:
        return f'fizzbuzz, {n} é divisivel por 3'
    if n % 3 == 0:
        return f'fizzbuzz, {n} é divisivel por 5'
    return n

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))






