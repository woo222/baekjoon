import sys

board = []

for i in range(19):
    board.append(list(map(int, input().split())))

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] != 0:
            omok = board[i][j]

            for k in range(4):
                cnt = 1
                x = i + dx[k]
                y = j + dy[k]

                while 0 <= x < 19 and 0 <= y < 19 and board[x][y] == omok:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 and board[i - dx[k]][j - dy[k]] == omok:
                            break
                        if 0 <= x + dx[k] < 19 and 0 <= y + dy[k] < 19 and board[x + dx[k]][y + dy[k]] == omok:
                            break
                        
                        print(omok)
                        print(i + 1, j + 1)
                        sys.exit(0)

                    x += dx[k]
                    y += dy[k]

print(0)