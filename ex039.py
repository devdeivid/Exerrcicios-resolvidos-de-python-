#Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se ja passou do tempo do aalistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou
# do prazo.
from datetime import date
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento? '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Voce ja deveria ter se alistado ha {saldo}anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')

