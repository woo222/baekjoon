'''
BFS로 풀어보자
u, d 두 경우 모두 계산해보고
배열에 버튼 누른 횟수 count
이미 가본 적이 있는 층이거나 범위를 벗어날 경우 종료
'''
from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0] * (f+1)

def bfs_start():
    queue = deque([s])
    visited[s] = 1
    while queue:
        v = queue.popleft()
        if v == g:
            return (visited[v]-1)
        else:
            for i in (v+u, v-d):
                # 범위 확인
                if 0<i<=f and visited[i] == 0:
                    visited[i] = visited[v] + 1
                    queue.append(i)
    return 'use the stairs'
            

print(bfs_start())