import os
from termcolor import colored

restaurantes = ["Pizza", "Hamburguer"]

def exibir_nome_do_programa():
    print(colored("""
 ██████╗ █████╗ ██████╗  █████╗ ██████╗   ███████╗██╗  ██╗██████╗ ██████╗ ███████╗ ██████╗ ██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗ ███████║██████╦╝██║  ██║██████╔╝  █████╗   ╚███╔╝ ██████╔╝██████╔╝█████╗  ╚█████╗ ╚█████╗ 
 ╚═══██╗██╔══██║██╔══██╗██║  ██║██╔══██╗  ██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██╗██╔══╝   ╚═══██╗ ╚═══██╗
██████╔╝██║  ██║██████╦╝╚█████╔╝██║  ██║  ███████╗██╔╝╚██╗██║     ██║  ██║███████╗██████╔╝██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝  ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ 
""", "yellow"))

def exibir_opcoes():
    print(colored("1. ", "white") + colored("Cadastrar restaurante", "yellow"))
    print(colored("2. ", "white") + colored("Listar restaurantes", "yellow"))
    print(colored("3. ", "white") + colored("Ativar restaurante", "yellow"))
    print(colored("4. ", "white") + colored("Sair\n", "yellow"))

def finalizar_app():
    os.system("cls")
    print(colored("Finalizando o app\n", "green"))

def opcao_invalida():
    print(colored("Opção inválida!\n", "red"))
    input(colored("Digite uma tecla para voltar ao menu principal: ", "cyan"))
    main()

def cadastrar_novo_restaurante():
    os.system("cls")
    print(colored("=-" * 15, "white"))
    print(colored("Cadastro de novos restaurantes", "yellow"))
    print(colored("=-" * 15, "white"))

    nome_do_restaurante = input(colored("\n• Digite o nome do restaurante que deseja cadastrar: ", "yellow"))
    restaurantes.append(nome_do_restaurante)
    print(colored(f"• O restaurante ", "yellow") + colored(nome_do_restaurante, "green") + colored(" foi cadastrado com sucesso!\n", "yellow"))

    print(colored("=-" * 24, "white"))
    input(colored("Pressione ENTER para voltar ao menu principal... ", "yellow"))
    main()

def listar_restaurantes():
    os.system("cls")
    print(colored("=-" * 15, "white"))
    print(colored(f"{"Listando restaurantes":^30}", "yellow"))
    print(colored("=-" * 15, "white"))
    print("")

    for restaurante in restaurantes:
        print(colored("• ", "white") + colored(restaurante, "yellow"))

    print("")
    print(colored("=-" * 24, "white"))
    input(colored("Pressione ENTER para voltar ao menu principal... ", "yellow"))
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input(colored("Escolha uma opção: ", "yellow")))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main() 