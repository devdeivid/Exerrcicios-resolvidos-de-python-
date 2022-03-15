#Elabore um programa que calcule o valor a ser pago por um produto, conciderando o seu
# preço normal e condiçao de pagamento:
#- á vista dinheiro/cheque:10% de desconto     -em até 2x no cartao:preço normal
#-á vista no cartao :5% de desconto            -3x ou mais no cartao:20% de juro

print('-=-=-=-=-=-=-=-=-= LOJAS DO DEIVID =-=-=-=-=-=-=-=-=-=')


preço = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO'
      '[ 1 ] á vista dinheiro/cheque'
      '[ 2 ] á vista cartao'
      '[ 3 ] 2x no cartao'
      '[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Qual é a opçao que deseja pagar? '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
    print(f'Seu preço a vista será R${total}.')
elif opçao == 2:
    total = preço - (preço * 5 / 100)
    print(f'Seu preço a vista no cartao será R${total}.')
elif opçao == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelado em 2x de {parcela}')
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra sera parcelada em {totparc:.2f}x de R${parcela:.2f} COM JUROS. ')
else:
    total = preço
    print('OPÇAO INVALIDA! de pagamento,  tente novamente.')
print(f'Sua compra de R${preço:.2f} vai custar {total:.2f}')







