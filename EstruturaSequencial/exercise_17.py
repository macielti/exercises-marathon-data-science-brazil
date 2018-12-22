'''17. Faça um Programa para uma loja de tintas. O programa deverá 
pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros 
quadrados e que a tinta é vendida em latas de 18 litros, que 
custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas 
    e os respectivos preços em 3 situações:

    a. comprar apenas latas de 18 litros;

    b. comprar apenas galões de 3,6 litros;

    c. misturar latas e galões, de forma que o preço seja o menor.
    Acrescente 10% de folga e sempre arredonde os valores para 
    cima, isto é, considere latas cheias.'''

area = float(input("Tamnho da área a ser pintada (m²): "))

litros_nessessarios =  area / 6.0

latas = litros_nessessarios / 18.0
latas_valor_total = latas * 80.0

galoes = litros_nessessarios / 3.6
galoes_valor_total = galoes * 25.0

print('\nLatas de 18 litros:', latas, 'latas')
print('Valor total:', latas_valor_total, 'reais')

print('\nGalões de 8,6 litros:', galoes, 'galões')
print('Valor total:', galoes_valor_total, 'reais')

litros_nessessarios += litros_nessessarios * 0.1


if (litros_nessessarios) >= 18:
    latas = int(litros_nessessarios  / 18.0)
    resto_de_litros = litros_nessessarios % 18.0
    #caso eu tenhas litros sobrando no resto do calculo de latas
    if resto_de_litros > 0:
        #caso o resto não dê um galão
        if resto_de_litros <= 3.6:
            galoes = 1
        #caso o resto passe de um galão
        else:
            galões = int(resto_de_litros / 3.6)
            #caso sobre litros no calculo dos galões
            if resto_de_litros % 3.6 > 0:
                galoes += 1


    else:
        galoes = 0
#caso os litros não sejam suficientes para um galão
else:
    latas = 0
    galoes = int(litros_nessessarios / 3.6)
    resto_de_litros = litros_nessessarios % 3.6
    #caso ainda sobre algum litro
    if resto_de_litros > 0:
        galoes += 1

print('\nMisturados\nLatas:', latas)
print('Galôes:', galoes)
print('Preço total:', latas * 80 + galoes * 25)
