from sys import stdin

n, m = map(int, stdin.readline().split())

basket = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, stdin.readline().split())
    tmp = basket[i:j+1]
    basket[i:j+1] = reversed(tmp)

for k in range(1, n+1):
    print(basket[k], end = ' ')