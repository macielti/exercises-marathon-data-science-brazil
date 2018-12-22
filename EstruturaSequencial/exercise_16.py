'''16. Faça um programa para uma loja de tintas. O programa deverá 
pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros 
quadrados e que a tinta é vendida em latas de 18 litros, que
custam R$ 80,00. Informe ao usuário a quantidades de latas de 
tinta a serem compradas e o preço total.'''

area = float(input("Tamnho da área a ser pintada (m²): "))

litros_nessessarios =  area / 3.0
latas = litros_nessessarios / 18.0
preco_total = latas * 80.0

print("\nQuantidade de latas:", latas)
print("Preço total:", preco_total)