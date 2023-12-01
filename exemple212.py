# Exemplo 2.12 - Uma lista com três listas de tamanho 3 pode representar um tabuleiro de jogo da velha

board = [['_']* 3 for i in range(3)]
print(board)

board = []
for i in range(3):
    row =['_']* 3 # O
    board.append(row)