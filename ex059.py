#Crie um programa que leia dois valores e mostre um menu como o
# ao lado na tela:  Seu programa deverá realizar a operaçao solicitada
# em cada caso.
#[1]somar  [2]multiplicar  [3]maior  [4]novos numeros  [5]sair do programa
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opçao = int(input('Qual é sua opçao? '))
    if opçao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} e {n2} é {soma}')
    elif opçao == 2:
        multiplicaçao = n1 * n2
        print(f'A multiplicaçao de {n1} e {n2} é de {multiplicaçao} ')
    elif opçao == 3:
        if n1 > n2:
            print(f'{n1} é Maior!')
        else:
            print(f'{n2} é maior!')
    elif opçao == 4:
        print('Informe novamente os 2 numeros! ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando')
    else:
        print('Opçao invalida!. Tente novamente!')
        print('-='*20)
print('Fim do programa! Volte sempre!')





