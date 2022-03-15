#Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar
# que tipo de triangulo será formado:
#-Equilatero: todos os lados iguais
#-Isosceles: dois lados iguais
#-Escaleno: todos os lados diferentes

print('-=-'*30)
print('Analalisador de triangulos ')
print('-=-'*30)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Treceiro segmento: '))
if r1 < r2 +3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo! ')
    if r1 and r2 and r3 == r1 and r2 and r3:
        print('Esse triangulo é um EQUILATERO!')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Esse triangûlo é um ISOCELIS!')
    else:
        print('Esse triângulo é um ESCALENO!')
else:
    print('Os segmento acima NAO PODEM FORMAR Triângulo! ')


