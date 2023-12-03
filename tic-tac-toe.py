board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = 1

def move(row, col, player):
    if board[row][col] == 0:
        board[row][col] = player
        if player == 1:
            player = 2
        else:
            player = 1
        return player
    else:
        print("Invalid move")

def is_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if (board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False

def print_board():
    for i in range(3):
        print(board[i])

for i in range(9):
    print_board()
    row = int(input(f"Enter your row player_{player} : "))
    col = int(input(f"Enter your column player_{player} : "))
    player = move(row, col, player)
    if is_winner(1):
        print("Player 1 wins!")
        break
    elif is_winner(2):
        print("Player 2 wins!")
        break
