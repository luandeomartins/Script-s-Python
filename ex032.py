from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será {}.'.format(lista))

# Sorteio de quatro nomes e uso do método shuffle para embaralhar as variáveis.
# Como nesse caso eu especifiquei qual o método que quero, a escrita é somente o método (variável a ser sorteada).
# Exemplo: shuffle(lista).