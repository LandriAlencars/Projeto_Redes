import socket
from random import choice

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogadores = ['X', 'O']
        self.jogador_atual = 0
        self.vencedor = None
        self.empate = False

    def fazer_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] != ' ' or self.vencedor is not None:
            return False
        
        self.tabuleiro[linha][coluna] = self.jogadores[self.jogador_atual]
        
        if self.verificar_vitoria():
            self.vencedor = self.jogadores[self.jogador_atual]
        elif self.verificar_empate():
            self.empate = True
        else:
            self.jogador_atual = (self.jogador_atual + 1) % 2
        
        return True

    def verificar_vitoria(self):
        # Verifica linhas
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != ' ':
                return True
        
        # Verifica colunas
        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != ' ':
                return True
        
        # Verifica diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return True
        
        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            if ' ' in linha:
                return False
        return True

    def estado_atual(self):
        estado = []
        for linha in self.tabuleiro:
            estado.extend(linha)
        estado.append(str(self.jogador_atual))
        return ','.join(estado)

    def carregar_estado(self, estado):
        dados = estado.split(',')
        for i in range(3):
            for j in range(3):
                self.tabuleiro[i][j] = dados[i*3 + j]
        self.jogador_atual = int(dados[9])
        self.vencedor = None
        self.empate = False
        if self.verificar_vitoria():
            self.vencedor = self.jogadores[(self.jogador_atual + 1) % 2]
        elif self.verificar_empate():
            self.empate = True

def main():
    host = '0.0.0.0'
    port = 5000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(2)  # Aceita até 2 conexões (2 jogadores)
    
    print("Servidor aguardando conexões...")
    
    # Aceita conexão do jogador 1
    conn1, addr1 = servidor.accept()
    print(f"Jogador 1 conectado: {addr1}")
    conn1.sendall('X'.encode())  # Jogador 1 é X
    
    # Aceita conexão do jogador 2
    conn2, addr2 = servidor.accept()
    print(f"Jogador 2 conectado: {addr2}")
    conn2.sendall('O'.encode())  # Jogador 2 é O
    
    jogo = JogoDaVelha()
    
    try:
        while True:
            # Envia estado do jogo para ambos os jogadores
            estado = jogo.estado_atual()
            conn1.sendall(estado.encode())
            conn2.sendall(estado.encode())
            
            if jogo.vencedor or jogo.empate:
                break
            
            # Determina qual conexão é a do jogador atual
            conn_atual = conn1 if jogo.jogador_atual == 0 else conn2
            
            # Recebe jogada do jogador atual
            data = conn_atual.recv(1024).decode()
            if not data:
                break
                
            linha, coluna = map(int, data.split(','))
            
            # Processa jogada
            if jogo.fazer_jogada(linha, coluna):
                print(f"Jogada recebida: {linha}, {coluna}")
            else:
                print("Jogada inválida recebida")
                
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        # Envia estado final
        estado_final = jogo.estado_atual()
        conn1.sendall(estado_final.encode())
        conn2.sendall(estado_final.encode())
        
        conn1.close()
        conn2.close()
        servidor.close()
        print("Conexões encerradas")

if __name__ == '__main__':
    main()