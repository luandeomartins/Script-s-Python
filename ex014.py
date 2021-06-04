largura = float(input('Qual é a largura da parede em metros? '))
altura = float(input('Qual é a altura da parede em metros? '))
area = largura * altura
quantidadetinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {} m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(quantidadetinta))
# Programa que mostra a quantidade de tinta à ser usada em cima da metragem
