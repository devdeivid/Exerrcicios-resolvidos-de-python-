#Desenvolva um programa #que leia o comprimento de tres nretas
# e diga ao usuario se elas podem ou nao  formar um triangulo.
print('-=-'*30)
print('Analalisador de triangulos ')
print('-=-'*30)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Treceiro segmento: '))
if r1 < r2 +3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo! ')
else:
    print('Os segmento acima NAO PODEM FORMAR Triângulo! ')