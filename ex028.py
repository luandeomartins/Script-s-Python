from math import radians,cos,sin,tan
angulo = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}.'.format(angulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}.'.format(angulo, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}.'.format(angulo, tangente))

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Neste exemplo, eu fiz importando apenas os métodos que foi usar no meu programa.
# Sendo assim, não necessita referenciar a biblioteca (cos(variável a ser aplicado o método))
# Como precisei transformar o número para radianos, escrevi cos(radians(variável a ser aplicado o método))
