# Jogo da Velha (Tic-Tac-Toe) no Terminal 🎮

Um clássico Jogo da Velha desenvolvido em Python para ser jogado diretamente no terminal. O jogo possui suporte a cores para facilitar a visualização e um sistema inteligente e flexível de validação de jogadas.

## 📸 Prints do Jogo

Abaixo estão as capturas de tela demonstrando o jogo em funcionamento:

### Início da Partida
> *Mostrando o tabuleiro vazio e as cores dos jogadores.*

<img width="644" height="255" alt="image" src="https://github.com/user-attachments/assets/3a76020d-d3da-4322-ad04-ca911a3f456b" />


### Jogada e Tabuleiro Preenchido
> *Demonstrando a validação de entrada de dados e as casas ocupadas.*

<img width="472" height="259" alt="image" src="https://github.com/user-attachments/assets/3120cf5c-a8a1-4a42-8500-1353f99cd3d9" />


### Fim de Jogo
> *Mensagem de vitória ou empate (Deu velha).*

<img width="293" height="238" alt="image" src="https://github.com/user-attachments/assets/9783bb32-9f92-4838-b162-54000ab02d4c" />


---

## ✨ Funcionalidades

* **Interface Colorida:** Utiliza códigos de escape ANSI para diferenciar visualmente os jogadores (X em vermelho, O em azul) e destacar mensagens importantes.
* **Entrada de Dados Flexível:** O sistema extrai apenas os números da entrada do jogador. Isso significa que você pode separar a linha e a coluna usando espaços, vírgulas, traços ou pontos (ex: `1 1`, `1,1`, `1-1` ou `1.1`) e o jogo entenderá perfeitamente.
* **Validação de Jogadas:** O jogo impede que os usuários joguem em posições que não existem (fora do intervalo 0-2) ou em casas que já estão ocupadas.
* **Verificação Automática:** Detecta automaticamente quando um jogador vence a partida ou quando o jogo empata ("Deu velha").

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

O tabuleiro é mapeado por um sistema de coordenadas que vai de `0` a `2` tanto para as linhas quanto para as colunas, seguindo este formato exato:

```text
 0,0 | 0,1 | 0,2 
-----|-----|-----
 1,0 | 1,1 | 1,2 
-----|-----|-----
 2,0 | 2,1 | 2,2
