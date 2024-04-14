estoque = [
    {'nome': 'maçã', 'preço': 2.0, 'quantidade': 5},
    {'nome': 'banana', 'preço': 1.5, 'quantidade': 10}
]

total_estoque = 0

for produto in estoque:

    total_produto = produto['preço'] * produto['quantidade']

    total_estoque += total_produto

print(f'\nValor total em produtos no estoque: R${total_estoque:.2f}\n')
