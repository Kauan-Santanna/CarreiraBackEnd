maca = int(input("Digite a quantidade de maçãs vendidas: "))
banana = int(input("Digite a quantidade de bananas vendidas: "))

if maca > banana:
    print("As maçãs tiveram mais vendas.")
elif maca < banana:
    print("As bananas tiveram mais vendas.")
else:
    print("As vendas foram iguais.")