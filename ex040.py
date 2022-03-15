#Crie um programa que leia duas notas de um aluno e calcule sua media,
# mostrando uma mensagem no final, de acordo como a media atingida:
# - Media abaixo de 5.0: REPROVADO
# - Media entre 5.0 e 6.9:RECUPERAÇAO
# - Media 7.0 ou superior:APROVADO
nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
media = (nota_2 + nota_1) / 2
print(f'Tirando {nota_1} e {nota_2} a media do aluno é {media:.1f}')
if media < 5.0:
    print('Voce esta REPROVADO!')
elif media <=6.9:
    print('Voce esta de RECUPERAÇAO!')
else:
    print('Voce esta APROVADO!')