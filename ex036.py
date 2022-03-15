#Escreva um programa para aprovar o eprestimo bancario para a compra
# de um imovel .Pergunte o valor da casa, o salario do comprador e em
# quantos anos ele vai pagar. A prestaçao mensal, nao pode exeder 30%
# do salario ou entao o emprestimo será negado.
casa = float(input('Qual valor do imovel?R$ '))
salario = float(input('Qual é seu salario mensal?R$ '))
anos = int(input('Quantos anos quer financiar? '))
prestaçao = casa/ (anos * 12)
minimo = salario * 30 /100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos')
print(f'a prestaçao será de R${prestaçao:.2f}')
if prestaçao <= minimo:
    print('Emprestimo APROVADO!' )
else:
    print('Emprestimo NEGADO')

