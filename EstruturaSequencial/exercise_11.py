'''11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo'''

int_1 = int(input("Digite o 1° número inteiro: "))
int_2 = int(input("Digite o 2° número inteiro: "))
real = float(input("Digite um número real: "))

print("\n(", int_1*2,") * (",int_2/2,") =", (int_1*2) * (int_2/2) )
print("(", int_1*3,") + (",real,") =", (int_1*2) * (real) )
print(str(real)+'³ =', real**3  )