import os
from termcolor import colored

restaurantes = [
    {"nome":"Pizza", "categoria":"Massa", "ativo":False}, 
    {"nome":"Hamburguer", "categoria":"Fritas", "ativo":True},
    {"nome":"Sushi", "categoria":"Japonesa", "ativo":True}
]

# ==============================
# FUNÇÕES AUXILIARES
# ==============================

def voltar_ao_menu_principal():
    input(colored("Pressione ENTER para voltar ao menu principal... ", "yellow"))
    main()

def limpar_tela():
    os.system("cls")

def exibir_separador(tamanho=15):
    print(colored("=-" * tamanho, "white"))

# ==============================
# FUNÇÕES DO SISTEMA
# ==============================

def cadastrar_novo_restaurante():
    limpar_tela()
    exibir_separador()
    print(colored("Cadastro de novos restaurantes", "yellow"))
    exibir_separador()

    nome_do_restaurante = input(colored("\n• Digite o nome do restaurante que deseja cadastrar: ", "yellow"))
    categoria = input(colored(f"• Digite o nome da categoria do restaurante ", "yellow") + colored(nome_do_restaurante, "white") + colored(": ", "yellow"))
    dados_do_restaurante = {"nome":nome_do_restaurante,
                            "categoria":categoria,
                            "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(colored(f"• O restaurante ", "yellow") + colored(nome_do_restaurante, "green") + colored(" foi cadastrado com sucesso!\n", "yellow"))

    exibir_separador(24)
    voltar_ao_menu_principal()

def listar_restaurantes():
    limpar_tela()
    exibir_separador()
    print(colored(f"{"Listando restaurantes":^30}", "yellow"))
    exibir_separador()
    print("")

    print(colored(f"{"Restaurante:".ljust(14)} | {"Categoria:".ljust(12)} | Status:", "white"))
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(colored("• ", "white") + colored(f"{nome_restaurante.ljust(12)} | {categoria.ljust(12)} | {ativo}", "yellow"))

    print("")
    exibir_separador(24)
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    limpar_tela()
    exibir_separador(16)
    print(colored("Alternando estado do restaurante", "yellow"))
    exibir_separador(16)

    nome_restaurante = input(colored("Digite o nome do restaurante que deseja alternar o estado: ", "yellow"))
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]

            mensagem = (
            colored(f"O restaurante {nome_restaurante} ", "yellow")
            + colored("foi ativado com sucesso", "green") 
            if restaurante["ativo"] 
            else
            colored(f"O restaurante {nome_restaurante} ", "yellow") 
            + colored("foi desativado com sucesso", "red"))
            print(mensagem)

    if not restaurante_encontrado:
        print(colored("O restaurante não foi encontrado", "red"))

    exibir_separador(24)
    voltar_ao_menu_principal()

def finalizar_app():
    limpar_tela()
    print(colored("Finalizando o app\n", "green"))

# ==============================
# MENU
# ==============================

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

def escolher_opcao():
    try:
        opcao_escolhida = int(input(colored("Escolha uma opção: ", "yellow")))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def opcao_invalida():
    print(colored("Opção inválida!\n", "red"))
    voltar_ao_menu_principal()

# ==============================
# PROGRAMA
# ==============================

def main():
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main() 
