'''
dfs로 풀면 좋을 듯
기준 점을 잡고 상하좌우 확인
한 번 접근한 좌표는 다시 접근하지 않기
'''

n = int(input())
house = []
h_map = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(n):
    h_map.append(list(map(int, input())))
    
def dfs_house(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if h_map[x][y] == 1:
        count += 1
        h_map[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs_house(nx, ny)
        return True
    return False

count = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs_house(i, j) == True:
            result += 1 # 단지 수 저장
            house.append(count) # 집 수 저장
            count = 0

print(result)
house.sort()
for i in house:
    print(i)