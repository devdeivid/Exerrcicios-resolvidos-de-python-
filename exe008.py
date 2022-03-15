#Escreva um programa que leia um valor em metros
#e exiba convertido em centimetros e milimetros.
    #KM HM DAM M DM CM MM
    #quilômetro – (km);
    #hectômetro – (hm);
    #decâmetro – (dam);
    #metro – (m);
    #decímetro – (dm);
    #centímetro – (cm);
    #milímetro – (mm).

'''tamanho = float(input('Digite um Numero '))
cm = tamanho * 100
mm = tamanho * 1000
print(f'Amedida de {tamanho}m corresponde a {cm}cm e {mm}mm')
km = tamanho / 1000
dm = tamanho / 2
print(f'A medida de {tamanho}m corresponde a {km}km e {dm}dm')
'''
'''medida = float(input('Uma distancia em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('a media  de  {}m coresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))'''
medida = float(input('Uma distancia em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A media de {}m corresponde a \n{km} \n{hm} \n{dam} \n{dm} \n{cm} \n{mm}'.format(medida, km, hm, dam, dm, cm, mm))