from configs import funcoes

def menu_principal():
    # Desenho do cabeçalho
    print(37 * "=") 
    print(f'{"JOKENPÔ":^37}')
    print(37 * "=" )
    
    # Tupla com as opções do Jogo  
    opcoes = ("Pedra", "Papel", "Tesoura", "Ver pontos", "Regra","Sair")
    
    # Será impresso o número a partir do 1 e o item da tupla
    for numero, opcao in enumerate(opcoes, 1):
        print(f"{numero} - {opcao}")
    
    # Fim do cabeçalho
    print(37 * "=")

def menu_pontos(dict_pontos):
    # Cabeçalho
    print(37 * "=")
    print(f"{'Menu de Pontos':^37}")
    print(37 * "=")
    
    # Pegando os pontos do dicionário e atribuindo as variáveis
    computador = f"Pontos do Computador: {dict_pontos['Computador']}"
    jogador = f"Pontos do Jogador: {dict_pontos['Jogador']}"
    empate = f"Pontos de Empate: {dict_pontos['Empate']}"
    
    # Imprimindo os variáveis com as cores determinadas
    funcoes.texto_vermelho(computador)
    funcoes.texto_verde(jogador)
    funcoes.texto_azul(empate)

def regra_jogo():
    # Cabeçalho
    print(37 * "=")
    print(f"{'Regras do Jogo':^37}")
    print(37 * "=")
    
    print("Pedra ganha de Tesoura\nTesoura ganha de Papel\nPapel ganha de Pedra ")
    
    return voltar()
    
def voltar():
    # Cabeçalho
    print(37 * "=")
    print("Deseja voltar ao menu principal?\n1 - Sim\n2 - Não")
    print(37 * "=")
    
    sair = input("\033[33mDigite uma opção válida: \033[m")
    
    return funcoes.opcao_sair(sair)