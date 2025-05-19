# 🕹️ Jogo da Velha em Rede (Python)

Este projeto implementa um **Jogo da Velha (Tic Tac Toe)** multiplayer usando sockets em Python. Um servidor gerencia o jogo entre dois clientes conectados, que interagem via terminal.
## 💼📊Participantes
Cleiber de Meireles da Silva Junnior
Landri José de Alencar Sousa
Leonardo Lima Barbosa Pereira
Matheus Almeida Souza

## 📁 Estrutura do Projeto

- `servidor.py`: Código do servidor que gerencia o estado do jogo e as conexões dos jogadores.
- `cliente.py`: Código do cliente que permite a um jogador se conectar ao servidor e jogar.

## 🚀 Como Executar

### 1. Inicie o servidor

Em um terminal:

```bash
python servidor.py
```

> O servidor escutará na porta `5000` e aguardará dois jogadores.

### 2. Inicie os clientes

Em dois terminais diferentes (ou em máquinas diferentes na mesma rede), execute:

```bash
python cliente.py
```

> Quando solicitado, insira o endereço IP do servidor (por exemplo, `127.0.0.1` para localhost ou o IP da máquina do servidor).

## 🎮 Regras do Jogo

- Dois jogadores participam: **X** e **O**.
- Os jogadores jogam alternadamente informando linha e coluna (de 0 a 2).
- O jogo termina com vitória de um jogador ou empate.
- O estado do jogo é atualizado em tempo real para ambos os clientes.

## 🧱 Requisitos

- Python 3.6

## 💡 Funcionalidades

- Conexão entre dois jogadores via rede usando sockets TCP.
- Interface simples em terminal.
- Verificação automática de vitória e empate.
- Validação de jogadas.

## 📌 Observações

- O cliente foi adaptado para solicitar o IP do servidor manualmente via `input()`.
- O código é simples e ideal para fins didáticos ou projetos de redes.
