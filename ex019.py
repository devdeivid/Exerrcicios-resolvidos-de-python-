#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude,ele lendo o nome deles e escrevendo o
# nome do escolhido.
from random import randint
n1 = str(input('Digite o primeiro aluno: '))
n2 = str(input('Digite o segundo aluno: '))
n3 = str(input('Digite o terceiro aluno: '))
n4 = str(input('Digite o quarto aluno: '))
n5 = str(input('Digite o quinto aluno: '))
alunos = [n1, n2, n3, n4, n5]
sorteio = randint.choices(alunos)
print(f'O aluno sorteado para apager o quadro é {sorteio}')