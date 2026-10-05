class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Nome: {self._nome} | Categoria: {self._categoria} | Ativo: {self.ativo}"

    def listar_restaurantes():
        print(f"{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}")
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"

restaurante_praca = Restaurante("praca", "Gourmet")
restaurante_pizza = Restaurante("pizza", "Italiana")

restaurantes = [restaurante_praca, restaurante_pizza]

Restaurante.listar_restaurantes()