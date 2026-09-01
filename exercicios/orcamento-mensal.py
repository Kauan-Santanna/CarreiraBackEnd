gastos = float(input("Digite o total de despesas do mês (R$): "))

if gastos > 3000:
    print("Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Você ainda está dentro do orçamento.")