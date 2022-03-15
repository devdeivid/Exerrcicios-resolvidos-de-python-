#Refaça o Desafio 051, lendo o primeiro termo ea razao de uma PA,
# mostrando os 10 primeiro termos da progressao usando a estrutura
# while.
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo += razao
    cont += 1