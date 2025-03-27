def is_valid_sudoku(board):
    # verificador de linhas
    for row in board:
        if not is_valid_unit(row):
            return False

    # verificador de colunas
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_unit(column):
            return False

    # verificador de grade 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]
            if not is_valid_unit(square):
                return False
    return True

    #validador
def is_valid_unit(unit):
    unit = [x for x in unit if x != 0]
    return len(unit) == len(set(unit))

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 4, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if not (is_valid_sudoku(board)):
    print("Tabuleiro inválido.")
else:
    print("Tabuleiro válido.")