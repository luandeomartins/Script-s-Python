dias = int(input('Quantos dias alugados? '))
quilometros = float(input('Quantos quilômetros rodados? '))
pago = dias * 60
km = quilometros * 0.15
total = pago+km
print('O total à pagar é R$ {:.2f}.'.format(total))
# Programa que calcula o valor à ser pago em cima da quantidade de dias
# e os quilômetros rodados.
