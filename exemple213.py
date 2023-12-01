# Exemplo 2.13 - Uma lista com três referências à mesma lista é inútil
white_board = [["_"] * 3] * 3
print(white_board)

board = []
row = ["_"] * 3

for i in range(3):
    board.append(row)
