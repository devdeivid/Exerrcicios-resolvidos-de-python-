#A confederaçao nacional de nataçao precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
#- Até 9 anos:MIRIM
#- Até 14 anos:INFANTIL
#- Até 19 anos:JUNIOR
#- Até 25 anos:SENIOR
#- Acima:MASTER
from datetime import date
atual = date.today().year
nasc = int(input('Qual ano de nascimento? '))
idade = atual - nasc
print(f'Seu ano de nascimento é {nasc} voce tem {idade} Anos de idade!')
if idade <= 9:
    print('Sua categoria é MIRIM!')
elif idade <=14:
    print('Sua categoria é INFANTIL!')
elif idade <= 19:
    print('Sua categoria é JUNIOR!')
elif idade <=25:
    print('Sua categoria é SENIOR!')
else:
    print('Sua categoria é MASTER!')