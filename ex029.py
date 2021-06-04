import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}.'.format(escolhido))

# Sortear quatro alunos

# Módulo random randomiza.
# Lista para o python é escrito dentro de colchetes.
# random.choice é uma escolha randômica, no caso escolha randômica da variável lista.
# choice é o método dentro da biblioteca random.
# OBSERVAÇÃO: no exercício 030, farei apenas com o método choice da biblioteca random.
