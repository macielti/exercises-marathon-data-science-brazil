'''4. Faça um Programa que verifique se uma letra digitada é 
vogal ou consoante.'''

letra = input('Digite uma letra: ')

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 
            'j', 'k', 'l', 'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

if letra in vogais:
    print('A letra é uma vogal.')
elif letra in consoantes:
    print('A letra é uma consoante.')
else:
    print('Você não digitou uma letra.')
