produtos = input("Digite os protudos separados por vírgulas: ").split(",")
precos = input("Digite os preços separados por vírgula: ").split(",")

for produto, preco in zip(produtos, precos):
    print(f"{produto.strip()}: {preco.strip()}")