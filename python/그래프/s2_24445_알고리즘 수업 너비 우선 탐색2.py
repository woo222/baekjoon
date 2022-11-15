from collections import deque
n, m, r = map(int, input().split())

bList = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    bList[a].append(b)
    bList[b].append(a)

for i in range(1, n+1):
    bList[i].sort(reverse=True)

def bfs(start):
    bfs_q = deque([start])
    visit = [0] * (n+1)

    visit[start] = 1
    cnt = 2

    while(bfs_q):
        node = bfs_q.popleft()

        for i in bList[node]:
            if(visit[i] == 0):
                bfs_q.append(i)
                visit[i] = cnt
                cnt += 1
    return visit

rst = bfs(r)

for i in range(1, n+1):
    print(rst[i])