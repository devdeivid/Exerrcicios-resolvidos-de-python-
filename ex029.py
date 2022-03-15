#Escreva um programa que leia a velocidade de um carro.Se ele ultrapassar
# 80Km/h, mostre uma mensagem dizendo que ele foi multado.A multa vai custar
# R$7.00 por cada km acima do limite.
vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    print(f'Voce foi multado. Utrapassou o limite de 80Km/h.  ')
    multa = (vel - 80) * 7
    print(f'Voce deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')