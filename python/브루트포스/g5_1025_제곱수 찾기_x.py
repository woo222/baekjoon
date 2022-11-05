n, m = map(int, input().split())
number = []
new_num = ''

for i in range(n):
    number.append(input())

for i in range(n):
    for j in range(m):
        new_num += number[i][j]
        