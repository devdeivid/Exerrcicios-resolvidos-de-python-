#Desenvolva um programa que leia as duas notas de um aluno
#calcule e mostre a sua media.


'''nota_1 = float(input('Digite a nota do aluno '))
nota_2 = float(input('Digite a segunda nota '))
n1 = (nota_1 + nota_2) / 2
print(f'A media entre {nota_1} e {nota_2} é igual a {n1}')'''
n1 = float(input('Digite a nota do primeiro semestre: '))
n2 = float(input('Digite a nota do segundo semestre: '))
n3 = (n1 + n2) /2

if n3 < 6:
    print(f'Você esta de recuperaçao!')
else:
    print(f'Você Está aprovado!')
print(f'A madia entre {n1} e {n2} é de {n3} ')


