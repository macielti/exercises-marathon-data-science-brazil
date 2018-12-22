'''9. Faça um Programa que leia três números e mostre-os em 
ordem decrescente.'''

num1 = float(input('Digite o numero 1: '))
num2 = float(input('Digite o numero 2: '))
num3 = float(input('Digite o numero 3: '))

numeros = []

if num1 <= num2 and num1 <= num3:
    numeros.append(num1)
    if num2 <= num3:
        numeros.append(num2)
        numeros.append(num3)
    else:
        numeros.append(num3)
        numeros.append(num2)

elif num2 <= num1 and num2 <= num3:
    numeros.append(num2)
    if num1 <= num3:
        numeros.append(num1)
        numeros.append(num3)
    else:
        numeros.append(num3)
        numeros.append(num1)

elif num3 <= num1 and num3 <= num2:
    numeros.append(num3)
    if num1 <= num2:
        numeros.append(num1)
        numeros.append(num2)
    else:
        numeros.append(num2)
        numeros.append(num1)

numeros.reverse()

print('Números na ordem decrescente:', '; '.join([str(num) for num in numeros]))