#Faça um programa que leia o nome completo de um pessoa.
#Mostrando em seguida o promeiro e o  ultimo nome separadamente.
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer te conhecer! ')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))