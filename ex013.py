carteira = float(input('Quantos reais você tem? '))
dolar = carteira / 5.76
euro = carteira / 6.79
iene = carteira / 0.053
print('Com R$ {:.2f}, você pode comprar US$ {:.2f}.'.format(carteira, dolar))
print('Com R$ {:.2f}, você pode comprar € {:.2f}.'.format(carteira, euro))
print('Com R$ {:.2f}, você pode comprar Ұ {:.2f}.'.format(carteira, iene))
# Programa que converte reais para dólar e euro.
