n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

li.sort()

for i in range(n):
    print(li[i])