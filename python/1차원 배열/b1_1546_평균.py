n = int(input())
num = list(map(int, input().split()))
max_n = max(num)

new_n = []
for i in num:
    new_n.append(i/max_n*100)

print(sum(new_n)/n)