from sys import stdin

n, m = map(int, stdin.readline().split())
basket = [i for i in range(n)]
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for k in range(n):
    print(basket[k] + 1, end=' ')

