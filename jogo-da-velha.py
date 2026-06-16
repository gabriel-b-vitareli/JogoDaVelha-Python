#define função para printar o tabuleiro
def prinTabuleiro(tab):
    # Criando uma lista para não mexer no tabuleiro original, apenas na exibição
    exibicao = []
    for i in range(9):
        if tab[i] == 1:
            exibicao.append("\033[31mX\033[m") # X Vermelho
        elif tab[i] == 2:
            exibicao.append("\033[34mO\033[m") # O Azul
        else:
            exibicao.append(" ")

    print("\n")
    print(f" {exibicao[0]} | {exibicao[1]} | {exibicao[2]} ")
    print("\033[37m---|---|---\033[m")
    print(f" {exibicao[3]} | {exibicao[4]} | {exibicao[5]} ")
    print("\033[37m---|---|---\033[m")
    print(f" {exibicao[6]} | {exibicao[7]} | {exibicao[8]} ")
    print("\n")

#define função que valida a jogada
def validaJogada(entrada):
    entrada_limpa = ""
    for c in entrada:
        if c.isdigit():
            entrada_limpa = entrada_limpa + c
        else:
            entrada_limpa = entrada_limpa + " "
            
    jogada = entrada_limpa.strip().split()

    if len(jogada) == 2: 
        l = int(jogada[0]) #linha
        c_coluna = int(jogada[-1])
        if (l == 0 or l == 1 or l == 2) and (c_coluna == 0 or c_coluna == 1 or c_coluna == 2):
            return True
    return False
    
#escopo das variaveis
velha = 1
haVencedor = False

#cria o tabuleiro do jogo
tabuleiro = [0,0,0,
             0,0,0,
             0,0,0]

jogadorDaVez = 1

#o jogo, literalmente po, o jogo
while haVencedor == False and velha <= 9:
    prinTabuleiro(tabuleiro)
    
    # Define a cor do texto do jogador da vez no input
    cor_jogador = "\033[31m" if jogadorDaVez == 1 else "\033[34m"
    entrada = input(f"Qual a sua jogada, {cor_jogador}Jogador {jogadorDaVez}\033[m? (linha coluna): ")
    
    if validaJogada(entrada) == True:
        entrada_limpa = ""
        for c in entrada:
            if c.isdigit():
                entrada_limpa = entrada_limpa + c
            else:
                entrada_limpa = entrada_limpa + " "
                
        jogada = entrada_limpa.split()
        
        linha = int(jogada[0])
        coluna = int(jogada[1])
        
        print(f"\033[32mLinha: {linha} | Coluna: {coluna}\033[m")
        
        if tabuleiro[3*linha+coluna] == 0:
            tabuleiro[3*linha+coluna] = jogadorDaVez
            
            if (tabuleiro[0] == jogadorDaVez and tabuleiro[1] == jogadorDaVez and tabuleiro[2] == jogadorDaVez) or (tabuleiro[3] == jogadorDaVez and tabuleiro[4] == jogadorDaVez and tabuleiro[5] == jogadorDaVez) or (tabuleiro[6] == jogadorDaVez and tabuleiro[7] == jogadorDaVez and tabuleiro[8] == jogadorDaVez) or (tabuleiro[0] == jogadorDaVez and tabuleiro[3] == jogadorDaVez and tabuleiro[6] == jogadorDaVez) or (tabuleiro[1] == jogadorDaVez and tabuleiro[4] == jogadorDaVez and tabuleiro[7] == jogadorDaVez) or (tabuleiro[2] == jogadorDaVez and tabuleiro[5] == jogadorDaVez and tabuleiro[8] == jogadorDaVez) or (tabuleiro[0] == jogadorDaVez and tabuleiro[4] == jogadorDaVez and tabuleiro[8] == jogadorDaVez) or (tabuleiro[2] == jogadorDaVez and tabuleiro[4] == jogadorDaVez and tabuleiro[6] == jogadorDaVez):
                haVencedor = True
            else:
                if jogadorDaVez == 1:
                    jogadorDaVez = 2
                else:
                    jogadorDaVez = 1
                velha += 1
        else: 
            print("\033[31mJogada inválida (posição ocupada), tente novamente\033[m")
    else:
        print("\033[31mJogada inválida, tente novamente\033[m")

# Mensagens de fim de jogo coloridas
if haVencedor == True:
    cor_vencedor = "\033[31m" if jogadorDaVez == 1 else "\033[34m"
    print(f"\033[32mParabéns pela vitória, {cor_vencedor}jogador {jogadorDaVez}\033[32m!!!\033[m")
else:
    print("\033[33mDeu velha.\033[m")
    
prinTabuleiro(tabuleiro)
