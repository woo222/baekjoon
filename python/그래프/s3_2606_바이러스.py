computer = int(input())
network = int(input())

virus = [[]for _ in range(computer+1)]
visit = [0] * (computer+1)

for i in range(network):
    a, b = map(int, input().split())
    virus[a].append(b)
    virus[b].append(a)

def dfs(start):
    visit[start] = 1
    for i in virus[start]:
        if(visit[i] == 0):
            dfs(i)

dfs(1)
print(sum(visit)-1)