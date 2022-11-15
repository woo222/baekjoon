import sys
sys.setrecursionlimit(10**5) # 임의로 재귀깊이 설정

n, m, r = map(int, input().split())
visit = [0] * (n+1)
dList = [[] for _ in range(n+1)]
cnt = 1

# dfs 함수
def dfs(start):
    global cnt
    visit[start] = cnt
    for i in dList[start]:
        if (visit[i] == 0):
            cnt += 1
            dfs(i)

# 그래프 입력 받기
for i in range(m):
    a, b  = map(int, input().split())
    dList[a].append(b)
    dList[b].append(a)

# 내림차순 정렬
for i in range(len(dList)):
    dList[i].sort(reverse=True)

dfs(r)

for i in range(1, n+1):
    print(visit[i])