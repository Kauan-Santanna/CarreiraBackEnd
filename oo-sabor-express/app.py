from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "gourmet")
restaurante_mexicano = Restaurante("mexican food", "mexicana")
restaurante_japones = Restaurante("japa", "japonesa")

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()