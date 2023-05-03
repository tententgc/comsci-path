def Winner(board):
    if board[0] == board[1] == board[2] != ' ':
        return True
    elif board[3] == board[4] == board[5] != ' ':
        return True
    elif board[6] == board[7] == board[8] != ' ':
        return True
    elif board[0] == board[3] == board[6] != ' ':
        return True
    elif board[1] == board[4] == board[7] != ' ':
        return True
    elif board[2] == board[5] == board[8] != ' ':
        return True
    elif board[0] == board[4] == board[8] != ' ':
        return True
    elif board[2] == board[4] == board[6] != ' ':
        return True


def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("----------------------------------------")


count = 0


def StartGame(board, r):
    global count
    if Winner(board) or " " not in board:
        count += 1
        printBoard(board)
        return True

    for i in range(9):
        if board[i] == " ":
            if r % 2 == 0:
                board[i] = "X"
            else:
                board[i] = "O"
            r += 1
            StartGame(board, r)
            board[i] = " "
            r -= 1


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
StartGame(board, 0)
print(count)