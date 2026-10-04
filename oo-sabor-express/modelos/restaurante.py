class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f"Nome: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}"

restaurante_praca = Restaurante("Praca", "Gourmet")
restaurante_pizza = Restaurante("Pizza", "Italiana")

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)