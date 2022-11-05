# 메모리의 크기를 n만큼 유지하는 것이 중요
from heapq import heappush, heappop

n = int(input())
heap = []

for i in range(n):
    for a in list(map(int, input().split())):
        if len(heap) < n:
            heappush(heap, a) # 빈 리스트면 push
        else:
            if(heap[0] < a):
                heappop(heap)
                heappush(heap, a)
print(heap[0])