# Jogo da Velha (Tic-Tac-Toe) no Terminal 🎮

Um clássico Jogo da Velha desenvolvido em Python para ser jogado diretamente no terminal. O jogo possui suporte a cores para facilitar a visualização e um sistema inteligente e flexível de validação de jogadas.

## ✨ Funcionalidades

* **Interface Colorida:** Utiliza códigos de escape ANSI para diferenciar visualmente os jogadores (X em vermelho, O em azul) e destacar mensagens importantes.
* **Entrada de Dados Flexível:** O sistema extrai apenas os números da entrada do jogador. Isso significa que você pode separar a linha e a coluna usando espaços, vírgulas, traços ou pontos (ex: `1 1`, `1,1`, `1-1` ou `1.1`) e o jogo entenderá perfeitamente.
* **Validação de Jogadas:** O jogo impede que os usuários joguem em posições que não existem (fora do intervalo 0-2) ou em casas que já estão ocupadas.
* **Verificação Automática:** Detecta automaticamente quando um jogador vence a partida ou quando o jogo empata ("Deu velha").

## 📸 Capturas de Tela

*(Substitua os links abaixo pelas imagens do seu jogo rodando)*

| Início do Jogo | Vitória | Deu Velha |
| :---: | :---: | :---: |
| ![Início](caminho/para/print_inicio.png) | ![Vitória](caminho/para/print_vitoria.png) | ![Velha](caminho/para/print_velha.png) |

## 🚀 Como Executar

**Pré-requisitos:**
* Ter o [Python](https://www.python.org/) (versão 3.x) instalado na sua máquina.

**Passo a passo:**
1. Salve o código em um arquivo chamado `jogo_da_velha.py` (ou o nome de sua preferência).
2. Abra o terminal (ou prompt de comando).
3. Navegue até a pasta onde o arquivo foi salvo.
4. Execute o comando:

    ```bash
    python jogo_da_velha.py
    ```

## 🕹️ Como Jogar

O tabuleiro é mapeado por um sistema de coordenadas que vai de `0` a `2` tanto para as linhas quanto para as colunas, seguindo este formato:

    Linha 0:  (0,0) | (0,1) | (0,2) 
             -------|-------|-------
    Linha 1:  (1,0) | (1,1) | (1,2) 
             -------|-------|-------
    Linha 2:  (2,0) | (2,1) | (2,2) 

1. O jogo pedirá a jogada do **Jogador 1** (X) ou do **Jogador 2** (O).
2. Digite o número da linha, um separador (como espaço ou vírgula) e o número da coluna. Exemplo: para jogar no meio do tabuleiro, digite `1 1`.
3. O jogo alternará os turnos automaticamente até que alguém vença ou não haja mais espaços disponíveis.
