#Desenvolva um programa que leia o primeiro termo e a razao de
# uma PA. No final, mostre os 10 primeiros termos dessa progressao.
print('=='*20)
print('      10 TERMOS DE UM PA')
print('=='*20)
primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZAO: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}',end=' ')
print('ACABOU')

