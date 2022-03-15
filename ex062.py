#Melhore o Desafio 061, perguntando para o usuario se ele quer
# mostrar mais alguns termos. O programa ecerra quando ele disser
# que quer mostrar O termos.
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} - ', end='')
        termo += razao
        cont += 1
    print('PÁUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais ?'))
print(f'Progressao finalizada com {total} termos mostrados')






