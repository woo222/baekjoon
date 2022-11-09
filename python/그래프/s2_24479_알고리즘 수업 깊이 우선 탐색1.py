import sys
sys.setrecursionlimit(10**6)        # 파이썬의 최대 재귀 깊이를 크게 변경

n, m, r = map(int, sys.stdin.readline().split())
dfs_l = [[] for _ in range(n+1)]    # 연결된 정점 배열
visit = [0] * (n+1)                 # 방문한 정점 배열
cnt = 1                             # 몇 번 째 방문 했는지 확인

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dfs_l[a].append(b)
    dfs_l[b].append(a)

def dfs(R):
    global cnt
    visit[R] = cnt
    dfs_l[R].sort()
    for i in dfs_l[R]:
        if visit[i] == 0:
            cnt += 1
            dfs(i)


dfs(r)

for i in range(1, n+1):
    print(visit[i])