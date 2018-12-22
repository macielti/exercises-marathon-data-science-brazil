'''6. Faça um Programa que leia três números e mostre 
o maior deles. '''

num_1 = float(input('1° número: '))
num_2 = float(input('2° número: '))
num_3 = float(input('3° número: '))

maior = 0

if num_1 >= num_2 and num_1 >= num_3:
    maior = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    maior = num_2
elif num_3 >= num_1 and num_3 >= num_2:
    maior = num_3

print('\nMaior:', maior)
