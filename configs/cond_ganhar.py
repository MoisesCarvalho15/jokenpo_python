from random import choice
from configs.funcoes import texto_azul, texto_vermelho, texto_verde

# Lista das opções
opcoes = ("pedra", "papel", "tesoura")

def ganhador(op_user, dict_pontos):
    
    # Gera a opção aleatória do computador
    op_computador = choice(opcoes)
    
    # Empate
    if op_user == op_computador:
        texto_azul("Empatou")
        print(f"Você escolheu: {op_user.capitalize()}")
        print(f"Computador escolheu: {op_computador.capitalize()}")
        dict_pontos["Empate"] += 1
    
    # Computador Vence
    elif op_user == "pedra" and op_computador == "papel" \
        or op_user == "papel" and op_computador == "tesoura" \
        or op_user == "tesoura" and op_computador == "pedra":
        
        texto_vermelho("Computador Venceu!")
        print(f"Você escolheu: {op_user.capitalize()}")
        print(f"Computador escolheu: {op_computador.capitalize()}")
        dict_pontos["Computador"] += 1
    
    # Jogador Vence
    else:
        texto_verde("Você venceu!")
        print(f"Você escolheu: {op_user.capitalize()}")
        print(f"Computador escolheu: {op_computador.capitalize()}")
        dict_pontos["Jogador"] += 1