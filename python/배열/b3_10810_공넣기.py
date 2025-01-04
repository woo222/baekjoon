from sys import stdin

n, m = map(int, stdin.readline().split())
basket = [0] * n

for _ in range(m):
    i, j, k = map(int, stdin.readline().split())

    for a in range(i-1, j):
        basket[a] = k

for res in basket:
    print(res, end=' ')