def paint(board):
    result = []
    for i in range(len(board)-7):
        for j in range(len(board[i])-7):

            white_first = 0
            black_first = 0

            for a in range(i, i+8):
                for b in range(j, j+8):
                    if (a+b) % 2 == 0:
                        if board[a][b] != 'W':
                            white_first += 1
                        if board[a][b] != 'B':
                            black_first += 1
                    else:
                        if board[a][b] != 'B':
                            white_first += 1
                        if board[a][b] != 'W':
                            black_first += 1

            result.append(white_first)
            result.append(black_first)

    return result

height, length = map(int, input().split())
new_board = []

for _ in range(height):
    new_board.append(input())

print(min(paint(new_board)))