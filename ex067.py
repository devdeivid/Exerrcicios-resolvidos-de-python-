#Faça um programa que mostre a tabuada de varios números,
#um de cada vez, para cada valor digitado pelo usuario.
# O programa será interronpido quando o numero solicitado
# for negativo.
num = 0
while True:
    num = int(input('Que tabuada você quer? '))
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c} = {c*num}')

print('FIM DO PROGRAMA VOLTE SEMPRE!')





