'''5. Faça um programa para a leitura de duas notas parciais de 
um aluno. O programa deve calcular a média alcançada por aluno e 
apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou 
    igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual 
    a dez.'''

nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite o 2º nota: '))

media =  (nota1+nota2)/2.0

if media >= 7 and media < 10:
    print("Média:", media, '\nAprovado.')
elif media >= 10:
    print("Média:", media, '\nAprovado com Distinção.')
else:
    print('Reprovado')