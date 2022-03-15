#Crier um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos Dolares ela pode comprar.
num = float(input('Digite o valor em reais que voce tem na sua carteira:R$'))
dolar = num / 5.12
euro = num / 5.70
libra = num / 6.81

print(f'Com R${num:.2f} você pode comprar US${dolar:.2f} E${euro:.2f} L${libra:.2f}')
