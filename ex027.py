import math
angulo = float(input('Digite um ângulo qualquer: '))
seno = (math.sin(math.radians(angulo)))
cosseno = (math.cos(math.radians(angulo)))
tangente = (math.tan(math.radians(angulo)))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Neste exemplo, eu fiz importando a biblioteca inteira math. No ex028, farei a mesma coisa só que escolhendo as
# bibliotecas que quero usar.
# Como importei a biblioteca math inteira, preciso escrever (math.cos(math.radians(angulo)))
# Explicando a escrita, (biblioteca.metodo(biblioteca.metodo(variavel que desejo aplicar o método)))
