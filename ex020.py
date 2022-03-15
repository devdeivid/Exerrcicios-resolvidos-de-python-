#O mesmo professor do desafio anterior quer sortear a ordem de
# apresentaçao de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
n1 = str(input('Digite o primeiro aluno: '))
n2 = str(input('Digite o segundo aluno: '))
n3 = str(input('Digite o terceiro aluno: '))
n4 = str(input('Digite o quarto aluno: '))
n5 = str(input('Digite o quinto aluno: '))
alunos = [n1, n2, n3, n4, n5]
random.shuffle(alunos)
print(f'A ordem de apresentaçao será ')
print(alunos)