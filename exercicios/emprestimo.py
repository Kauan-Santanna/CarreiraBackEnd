renda_mensal = int(input("Digite o valor da sua renda mensal: "))
parcela = int(input("Digite o valor da parcela desejada: "))

if renda_mensal > 2000 and parcela <= 0.3 * renda_mensal:
    print("Empréstimo aprovado.")
elif renda_mensal <= 2000:
    print("Empréstimo negado: renda insuficiente.")
else:
    print("Empréstimo negado: parcela acima de 30% de renda.")