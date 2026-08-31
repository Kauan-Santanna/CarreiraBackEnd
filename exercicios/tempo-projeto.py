atividade_A = int(input("Informe os dias para a atividade A:"))
atividade_B = int(input("Informe os dias para a atividade B:"))
atividade_C = int(input("Informe os dias para a atividade C:"))

if (atividade_A >= 0 and atividade_B >= 0 and atividade_C >= 0):
    tempo_total = atividade_A + atividade_B + atividade_C
    print(f"O tempo total do projeto é de {tempo_total} dias.")
else:
    print("Erro: Os dias não pode ser negativos.")