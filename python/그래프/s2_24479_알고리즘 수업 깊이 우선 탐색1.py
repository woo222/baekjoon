import sys
n, m, r = map(int, input().split())
dfs_l = [[] for _ in range(n+1)]    # 연결된 정점 배열

for i in range(m):
    a, b = map(int, input().split())
    dfs_l[a].append(b)
    dfs_l[b].append(a)

for i in range(1, n+1):
    dfs_l[i].sort(reverse=True)

def dfs(R):
    stack = [r]
    visit = [0] * (n+1)                 # 방문 여부 배열
    result = [0] * (n+1)                # 방문 순서
    cnt = 1                             # 몇 번 째 방문 했는지 확인

    while stack:
        node = stack.pop()
        if visit[node] == 1:
            continue
        visit[node] = 1
        result[node] = cnt
        cnt += 1

        for i in dfs_l[node]:
            if visit[i] == 0:
                stack.append(i)

    return result

rst = dfs(r)

for i in rst[1:]:
    print(i)