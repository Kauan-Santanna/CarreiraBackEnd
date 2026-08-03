print("""
 ██████╗ █████╗ ██████╗  █████╗ ██████╗   ███████╗██╗  ██╗██████╗ ██████╗ ███████╗ ██████╗ ██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗ ███████║██████╦╝██║  ██║██████╔╝  █████╗   ╚███╔╝ ██████╔╝██████╔╝█████╗  ╚█████╗ ╚█████╗ 
 ╚═══██╗██╔══██║██╔══██╗██║  ██║██╔══██╗  ██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██╗██╔══╝   ╚═══██╗ ╚═══██╗
██████╔╝██║  ██║██████╦╝╚█████╔╝██║  ██║  ███████╗██╔╝╚██╗██║     ██║  ██║███████╗██████╔╝██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝  ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ 
""")

print("1. Cadastrar restaurante")
print("2. Listar restaurantes")
print("3. Ativar restaurante")
print("4. Sair\n")

opcao_escolhida = input("Escolha uma opção: ")
print(f"Você escolheu a opçao {opcao_escolhida}")

if opcao_escolhida == "1":
    print("Cadastrar restaurante")
elif opcao_escolhida == "2":
    print("Listar restaurantes")
elif opcao_escolhida == "3":
    print("Ativar restaurante")
elif opcao_escolhida == "4":
    print("Encerrando o programa")
else:
    print("Alternativa incorreta!")