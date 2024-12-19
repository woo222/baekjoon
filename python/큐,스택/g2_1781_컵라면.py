from sys import stdin
import heapq
n = int(stdin.readline().strip())
quest = []
for _ in range(n):
    quest.append(list(map(int,stdin.readline().split())))

quest.sort()

res = []

for i in quest:
    heapq.heappush(res, i[1])
    if i[0] < len(res):
        heapq.heappop(res)
print(sum(res))