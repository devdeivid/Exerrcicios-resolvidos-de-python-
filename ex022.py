#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas letras maiuscolas e minuscolas.
#Quantas letras ao todo(sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite um nome completo: ')).strip()
print('Analizando seu nome...')
print(f'Seu nome em letras maiuscolas é {nome.upper()}')
print(f'Seu nome em letras minuscolas é {nome.lower()}')
print(f'Seu nome tem  {len(nome)} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')



