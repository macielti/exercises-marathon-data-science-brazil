'''7. Faça um Programa que leia três números e mostre o maior 
e o menor deles.'''

numeros = []

for i in range(3):
    numeros.append(float(input("Digite o "+str(i+1)+'º '+'número: ')))

maior = numeros[0]
menor = numeros[0]
for num in numeros[1:]:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print('Maior:', maior)
print('Menor:', menor)
     