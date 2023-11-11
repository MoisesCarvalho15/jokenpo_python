from configs import cond_ganhar, menus, funcoes

def iniciar():
    # Dicionário dos pontos do jogo
    pontos = {"Jogador": 0, "Computador": 0, "Empate": 0}

    # Loop do Jogo
    while True:
        funcoes.limpar_tela()
        menus.menu_principal()
        
        op = input("\033[33mDigite uma das opções disponíveis: \033[m")
        
        funcoes.limpar_tela()

        if op == "1" or op.lower() == "pedra":
            op = "pedra"
            cond_ganhar.ganhador(op, pontos)
            funcoes.esperar()
            funcoes.limpar_tela()
            continue
        
        elif op == "2" or op.lower() == "papel":
            op = "papel"
            cond_ganhar.ganhador(op, pontos)
            funcoes.esperar()
            funcoes.limpar_tela()
            continue
        
        elif op == "3" or op.lower() == "tesoura":
            op = "tesoura"
            cond_ganhar.ganhador(op, pontos)
            funcoes.esperar()
            funcoes.limpar_tela()
            continue
        
        # Usuário escolheu ver pontos
        elif op == "4" or op.lower() == "ver pontos":
            menus.menu_pontos(pontos)
            menus.voltar()
            continue
        
        elif op == "5" or op.lower() == "regra":
            menus.regra_jogo()
            funcoes.limpar_tela()
            continue
        
        
        # Usuário escolheu sair
        elif op == "6" or op.lower() == "sair":
            funcoes.texto_vermelho("Saindo do programa...\nAté a próxima!")
            break
        
        # Usuário digitou nenhuma das opções disponíveis
        else:
            funcoes.texto_vermelho("Digite uma opção válida!")
            funcoes.esperar()
            funcoes.limpar_tela()
            continue

iniciar()