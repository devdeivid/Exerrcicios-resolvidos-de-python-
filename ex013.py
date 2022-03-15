#Faça um algoritimo que leia o salario de um funcionario e
# leia seu novo sdalario,com desconto de 15%.de aumento.
salario = float(input('Qual é o salario do funcionario? R$'))
aumento = salario + (salario * 15 / 100)
prazo = salario - (salario * 8 / 100)
print(f'Um funcionario que ganhava R${salario}, com 15% de aumento passa a receber R${aumento}')
print(f'Se o pagamento for com 8% de desconto ele irá receber R${prazo}')