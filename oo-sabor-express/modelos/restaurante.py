class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Nome: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}"

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"Nome: {restaurante.nome} | Categoria: {restaurante.categoria} | Ativo: {restaurante.ativo}")

restaurante_praca = Restaurante("Praca", "Gourmet")
restaurante_pizza = Restaurante("Pizza", "Italiana")

restaurantes = [restaurante_praca, restaurante_pizza]

Restaurante.listar_restaurantes()