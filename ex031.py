import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será {}.'.format(lista))

# Sorteio de quatro nomes e uso do método shuffle para enbaralhar as variáveis.
# Como nesse caso eu importei a biblioteca random, precisei refenciar escrevendo random.shuffle(lista).
# Explicando a escrita -> biblioteca.metodo(variável a ser embaralhada).
# No ex032, farei apeas especificando o método que irei usar.
