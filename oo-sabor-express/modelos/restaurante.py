class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Nome: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}"

    def listar_restaurantes():
        print(f"{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}")
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"

restaurante_praca = Restaurante("Praca", "Gourmet")
restaurante_pizza = Restaurante("Pizza", "Italiana")

restaurantes = [restaurante_praca, restaurante_pizza]

Restaurante.listar_restaurantes()