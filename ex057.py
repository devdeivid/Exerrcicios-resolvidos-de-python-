#Faça um programa que leia o sexo de uma pessoa, mas só aceite4 os valores
# 'M'ou 'F' caso esteja errado, peça a digitaçao novamente até ter um valor
# correto.
sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com suceso')