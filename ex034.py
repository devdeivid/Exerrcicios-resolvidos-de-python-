#Escreva um programa que pergunte o salario de um funcionario
# e calcule o valor do seu aumento.Para os salarios superiores
# a R$1250,00, Calcule um aumento de 10%.Para os inferiores ou
# iguais, o aumentoé de 15%.
salario = float(input('Qual é o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f}')