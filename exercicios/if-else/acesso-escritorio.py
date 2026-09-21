horario = int(input("Digite a hora atual (formato 24 horas): "))

if horario >= 8 and horario < 18:
    print("Acesso permitido.")
else:
    print("Acesso negado.")