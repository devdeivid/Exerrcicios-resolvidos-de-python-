#Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou nao com nome "santo".
cid = str(input('Em que cidade você naqsceu? ')).strip()
print(cid[:5].upper() == 'SANTO')