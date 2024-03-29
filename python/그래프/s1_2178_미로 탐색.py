from collections import deque

n, m = map(int, input().split())
maze = []

for i in range(n):
    tmp = input()
    maze.append([int(x) for x in tmp])

def bfs(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    queue_m = deque()
    queue_m.append([x, y])

    while queue_m:
        a, b = queue_m.popleft()

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if maze[x][y] == 0:
                continue

            if maze[x][y] == 1:
                maze[x][y] = maze[a][b] + 1
                queue_m.append([x, y])
    return maze[n-1][m-1]

print(bfs(0, 0))