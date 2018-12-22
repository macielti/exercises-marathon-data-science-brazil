'''15. Faça um Programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. Calcule e mostre o total 
do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o 
sindicato, faça um programa que nos dê:

    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela 
    abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.'''

val_hora = float(input("Quanto você ganha por hora? "))
num_horas = float(input("Quantidade de horas trabalhadas no mês: "))

sal_bruto = num_horas * val_hora
imp_renda = sal_bruto * 0.11
inss = sal_bruto * 0.08
sindicato = sal_bruto * 0.05
sal_liqui = sal_bruto - (imp_renda + inss + sindicato)

print("\n + Salário bruto:", sal_bruto, 'R$')
print(' - IR (11%):', imp_renda, 'R$')
print(' - INSS (8%):', inss ,'R$')
print(' - Sindicato (5%):', sindicato, 'R$')
print(' = Salário Liquido:', sal_liqui, 'R$')
