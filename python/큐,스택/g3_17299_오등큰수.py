from sys import stdin
a_len = int(stdin.readline().strip())
a = list(map(int, stdin.readline().strip().split()))

cnt_a = [0] * 1000001
stack = []
res = [-1] * a_len

for i in a:
    cnt_a[i] += 1

for i in range(a_len):
    while stack and cnt_a[a[stack[-1]]] < cnt_a[a[i]]:
        res[stack.pop()] = a[i]
    stack.append(i)

print(*res)