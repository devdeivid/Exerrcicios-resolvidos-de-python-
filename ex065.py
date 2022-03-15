#Crie um programa que leia varios numeros inteiros pelo teclado.No final de execuçao,
# mostre a media entre todos os valores e qual foi o maior e monor valores lidos.
# O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'sS':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maioir = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e media foi {media}')
print(f'O maior Valor foi {maior} e o menor foi {menor} ')

