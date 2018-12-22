'''8. Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar, sabendo que a decisão é 
sempre pelo mais barato.'''

prod_1 = float(input('Digite o preço do primero produto:'))
prod_2 = float(input('Digite o preço do primero produto:'))
prod_3 = float(input('Digite o preço do primero produto:'))

menor = 0

if prod_1 <= prod_2 and prod_1 <= prod_3:
    menor = prod_1
elif prod_2 <= prod_1 and prod_2 <= prod_3:
    menor = prod_2
elif prod_3 <= prod_1 and prod_3 <= prod_2:
    menor = prod_3


print('Você deve comprar o poduto que custa:', menor)