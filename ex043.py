#Desenvolva uma logica que leia o peso e a autura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#- Abaixo de 18,5: Abaixo do peso       - 25 até 30:Sobrepeso
#- Entre 18,5 E 25:Peso ideal                - 30 até 40:Obesidade
#                                       - Acima de 40:Obesidade morbida
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
print(f'Seu indice de massa corporia é de {imc:.1f}.')
if imc <= 18.5:
    print('ABAIXO DO PESO!')
elif imc <= 25:
    print('PESO IDEAL!')
elif imc <= 30:
    print('SOBREPESO!')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA!')