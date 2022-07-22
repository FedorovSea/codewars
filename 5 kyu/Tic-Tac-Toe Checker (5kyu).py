def kres(board):
    if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        return 1
    if board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        return 1
    if board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        return 1
    if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
        return 1
    if board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
        return 1
    if board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
        return 1
    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        return 1
    if board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1:
        return 1

    if board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        return 2
    if board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        return 2
    if board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
        return 2
    if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
        return 2
    if board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
        return 2
    if board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
        return 2
    if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        return 2
    if board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 2:
        return 2
    for i in board:
        if 0 in i:
            return -1
    else:
        return 0
