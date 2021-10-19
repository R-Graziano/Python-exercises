def stringToIntList(text):
    intList = []
    for c in text:
        intList.append(int(c))
    return intList


def sudokuBoard():
    board = []
    for _ in range(10):
        while True:
            row = input("Ingrese 9 valores enteros entre 1 y 9 sin repetir para la fila: ")
            try:
                if len(row) != 9 or row.find('0'):
                    raise ValueError
                assert int(row)
                break
            except AssertionError:
                print('La fila no está compuesta por solo numeros.')
            except ValueError:
                print('La fila de dígitos no tiene 9 numeros exactos.')
        board.append(stringToIntList(row))
    return board

def checkRow(row):
    if sorted(row) == [i for i in range(1,10)]:
        return True
    else:
        return False

def checkColumn(row):
    return checkRow(row)

def checkSquare(sqrmatrix):
    sqrmatrix = [value for row in sqrmatrix for value in row]
    return checkRow(sqrmatrix)

def checkSudokuBoard(board):
    for i in range(9):
        if not(checkRow(board[i])):
            return 'No es válido.'

    for i in range(9):
        aux = []
        for j in range(9):
            aux.append(board[j][i])
        if not(checkColumn(aux)):
            return 'No es válido.'

    for j in range(3):
        for k in range(3):
            auxMatrix = [[],[],[]]
            for row in range(0,3):
                for column in range(0,3):
                    auxMatrix[row].append(board[row+(3*k)][column+(3*j)])
            if not(checkSquare(auxMatrix)):
                return 'No es válido.'
    
    return 'Si, es válido.'


board1 = [[2, 9, 5, 7, 4, 3, 8, 6, 1],
          [4, 3, 1, 8, 6, 5, 9, 2, 7],
          [8, 7, 6, 1, 9, 2, 5, 4, 3],
          [3, 8, 7, 4, 5, 9, 2, 1, 6],
          [6, 1, 2, 3, 8, 7, 4, 9, 5],
          [5, 4, 9, 2, 1, 6, 7, 3, 8],
          [7, 6, 3, 5, 2, 4, 1, 8, 9],
          [9, 2, 8, 6, 7, 1, 3, 5, 4],
          [1, 5, 4, 9, 3, 8, 6, 7, 2]]

board2 = [[1, 9, 5, 7, 4, 3, 8, 6, 2],
          [4, 3, 1, 8, 6, 5, 9, 2, 7],
          [8, 7, 6, 1, 9, 2, 5, 4, 3],
          [3, 8, 7, 4, 5, 9, 2, 1, 6],
          [6, 1, 2, 3, 8, 7, 4, 9, 5],
          [5, 4, 9, 2, 1, 6, 7, 3, 8],
          [7, 6, 3, 5, 2, 4, 1, 8, 9],
          [9, 2, 8, 6, 7, 1, 3, 5, 4],
          [2, 5, 4, 9, 3, 8, 6, 7, 1]]

myBoard = sudokuBoard()
checkSudokuBoard(myBoard)