from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Terceiro aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi: {}.'.format(escolhido))

# Sortear aluno
# Mesmo programa feito no ex029, porém importei apenas o método choice da biblioteca random
# Sendo assim, não preciso referenciar escrevendo: random.choice(variável). Posso escrever apenas choice(variável).
# Importante somente o método desejado, a escrito fica: metodo(variável).
