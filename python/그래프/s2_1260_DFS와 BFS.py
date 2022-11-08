from collections import deque

n, m, v = map(int, input().split())
lst = [[] for _ in range(n+1)]
visit_d = [0] * (n+1)
bfs_q = []

for i in range(m):
    a, b = map(int, input().split())
    
    lst[a].append(b)
    lst[b].append(a)
# 각 요소들 정렬
for i in range(1, n+1):
    lst[i].sort()
    
def dfs(start):
    visit_d[start] = 1
    print(start, end=' ')

    for i in lst[start]:
        if(visit_d[i] == 0):
            dfs(i)

def bfs(start):
    bfs_q = deque([start])
    visit_b = [0] * (n+1)

    visit_b[start] = 1

    while(bfs_q):
        find = bfs_q.popleft()

        print(find, end=' ')

        for i in lst[find]:
            if(visit_b[i] == 0):
                bfs_q.append(i)
                visit_b[i] = 1
        
dfs(v)
print()
bfs(v)