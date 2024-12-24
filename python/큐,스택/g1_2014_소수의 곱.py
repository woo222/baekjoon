from sys import stdin
import heapq

k, n = map(int, stdin.readline().split())
decimal = list(map(int, stdin.readline().split()))

heap = []

for i in decimal:
    heapq.heappush(heap, i)

for _ in range(n):
    n = heapq.heappop(heap)
    for i in decimal:
        heapq.heappush(heap, (n * i))

        if n % i == 0:
            break

print(n)