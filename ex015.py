produto = float(input('Digite o preço do produto: R$ '))
desconto = (produto * 5)/100
produto2 = (produto-desconto)
print('O produto que custava R$ {}, na promoção com 5% de desconto, vai custar R$ {:.2f}.'.format(produto, produto2))
# Programa que calcula o valor do produto com 5% de desconto.
