from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(ca, co)
print('A hipotenusa vai medir {:.2f}.'.format(hi))

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.

# 1) from math import hypot (estou importando o método hypot da biblioteca math)
# 2) para aplicar o método, escrevo hypot (variável ca, variável co), ficando hi = hypot (ca, co).

