'''3. Faça um Programa que peça dois números e imprima a soma.'''

numeros = []
for i in range(2):
    numeros.append(int(input('Digite o '+str(i+1)+'º número: ')))

print(numeros[0],'+',numeros[1],'=', sum(numeros))