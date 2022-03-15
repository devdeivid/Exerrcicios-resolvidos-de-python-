#Faça um algoritimo que leia o preço de um produto e mostre
#seu novo preço, com 5% de desconto
preco = float(input('Qual é o preço do produto? R$'))
desconto = preco - (preco * 5 / 100)
print(f'O produto que custava R${preco:.2f}, na promoçao com desconto de 5% vai custar R${desconto:.2f} ' )
