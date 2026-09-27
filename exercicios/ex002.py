def contar_caracteres(palavra):
    return len(palavra)

texto = input("Digite uma palavra: ")
print(f"Essa palavra tem {contar_caracteres(texto)} caracteres.")