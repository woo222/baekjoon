'''
그래프의 정보를 저장해야하므로 dfs 사용하는 것이 좋을 것 같다.
범위, 조건, 반복 잘 보기
-> 메모리 초과 오류..
bfs로 풀어보기
-> 해결
'''
from collections import deque
import sys

n = int(input())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_area(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and (area[nx][ny] > water) and (visit[nx][ny] == 0):
                visit[nx][ny] = 1
                queue.append((nx, ny))

max_area = 1
for water in range(max(map(max, area))):
    visit = [[0 for _ in range(n)] for i in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > water and visit[i][j] == 0:
                bfs_area(i, j)
                result += 1
    max_area = max(max_area, result)

print(max_area)

'''
이동할 수 있는 배열을 만들면 메모리 에러 발생 -> 입력받은 배열로 조건 설정 필요
# 재귀 최대 깊이 설정
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 안전지역 표시하기
def dfs_area(x, y, w):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and (area[nx][ny] > w) and not safe_area[nx][ny]:
            safe_area[nx][ny] = True
            dfs_area(nx, ny, w)

max_area = 1
for water in range(max(map(max, area))):
    safe_area = [[False] * n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > water and not safe_area[i][j]:
                safe_area[i][j] = True
                result += 1
                dfs_area(i, j, water)
    max_area = max(max_area, result)

print(max_area)
'''