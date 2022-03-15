#Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher,
# só que agora utilizando um laço for.
print('==================TABUADA USANDO FOR=================')
num = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c}')
