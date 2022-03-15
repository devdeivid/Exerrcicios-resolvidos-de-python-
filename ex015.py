#Escreva um programa que pergunte a quantidade de KM percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar,sabendo que o carro custa R$60 dia e
# R$0.15 por Km rodado.
dia = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos km o carro andou? '))

valor_aluguel = 60
valor_km = 0.15
n1 = dia * valor_aluguel
n2 = km * valor_km


print(f'O seu carro andou {km}km com {dia} dias e seu aluguel diario é de R${n1} e o aluguel rodado é de R${n2} ')