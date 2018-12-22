'''4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

notas = []
for i in range(4):
    notas.append(float(input('Digite a '+str(i+1)+'º nota: ')))

print("\nNotas:", "; ".join([str(nota) for nota in notas]), "\nMédia:", sum(notas)/4  )