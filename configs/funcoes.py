import time
import os
import platform
from configs.menus import menu_principal, voltar

def limpar_tela():
    # Capturando qual o modelo do Sistema Operacional
    sistema_operacional = platform.system()
    
    # Condicional para usar comandos de limpar a tela no terminal
    if sistema_operacional == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Espera 3 segundos
esperar = lambda: time.sleep(3)
    
def opcao_sair(op):
    if op == '1' or op.lower() == "sim":
        limpar_tela()
        menu_principal()
    elif op == '2' or op.lower() == "não" or op.lower() == "nao":
        limpar_tela()
        texto_vermelho("Saindo do programa...\nAté a próxima!")
        exit()
    else:
        limpar_tela()
        texto_vermelho("Digite uma opção válida")
        esperar()
        limpar_tela()
        voltar()
    return op

# Texto com cores no Terminal
def texto_azul(texto):
    print(f"\033[34m{texto}\033[m")
    return

def texto_vermelho(texto):
    print(f"\033[31m{texto}\033[m")
    return

def texto_verde(texto):
    print(f"\033[32m{texto}\033[m")
    return