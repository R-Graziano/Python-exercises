from random import randrange

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

# list comprehension board2 = [[i+(column*3) for i in range(1,4)] for column in range(0,3)]



def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    print(" +-------+-------+-------+\n",
          "|       |       |       |\n",
          "|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |\n",
          "|       |       |       |\n",
          "+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |\n",
          "|       |       |       |\n",
          "+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |\n",
          "|       |       |       |\n",
          "+-------+-------+-------+",)
          
         

def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    continuar = True
    while continuar:
        userMove = int(input("Ingresa tu movimiento:"))
        if 1 <= userMove <= 9:
            for row in board:
                if userMove in row: 
                    if userMove <= 3:
                        board[0][userMove-1] = "O"
                    elif userMove > 3 and userMove < 7:
                        board[1][userMove-4] = "O"
                    else:
                        board[2][userMove-7] = "O"
                    continuar = False
                    break
            else:
                print("Posición no válida...")
        else:
            print("Posición no válida...")
            
    DisplayBoard(board)
     
            
            
def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    freeFields = []
    for row in board:
        for value in row:
            if value in range(1,10):
                freeFields.append((board.index(row),row.index(value)))
    
    return freeFields
    
    
    
def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
    # Victoria horizontal
    for row in board:
        if [sign, sign, sign] == row:
            return True
    
    # Victoria vertical
    flat_board = [num for row in board for num in row]
    if (flat_board[0] == sign and flat_board[3] == sign and flat_board[6] == sign) \
       or (flat_board[1] == sign and flat_board[4] == sign and flat_board[7] == sign) \
       or (flat_board[2] == sign and flat_board[5] == sign and flat_board[8] == sign) :
        return True
    
    # Victoria diagonal
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) \
    or (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True
    
    return False


def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#   

    if board[1][1] != "X" and board[1][1] != "O":
        board[1][1] = "X"
    else:
        continuar = True
        while continuar:
            comMove = randrange(1,10)
            print("COM elige", comMove)
            for row in board:
                if comMove in row: 
                    if comMove <= 3:
                        board[0][comMove-1] = "X"
                    elif comMove > 3 and comMove < 7:
                        board[1][comMove-4] = "X"
                    else:
                        board[2][comMove-7] = "X"
                    continuar = False

    DisplayBoard(board)

BE = [[1,"O","O"],
      ["X","X","X"],
      ["O","X","O"]]


print(VictoryFor(BE, "O"))
print(MakeListOfFreeFields(BE))

#counter = 0
#DisplayBoard(board)
#while True:
#    counter += 1
#    print("Round ",counter)
#    DrawMove(board)
#    EnterMove(board)
#    if VictoryFor(board, "O"):
#        print("Ganador: USER")
#        break
#    if VictoryFor(board, "X"):
#        print("Ganador: COM")
#        break
#    if MakeListOfFreeFields(board) == []:
#        print("Hubo un empate.")
#        break
    