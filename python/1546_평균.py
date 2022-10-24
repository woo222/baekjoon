n = int(input())
num = list(map(int, input().split()))
max = num[0]
sum = 0

for i in range(1, n):
    if(num[i] > max):
        max = num[i]

for i in range(n):
    num[i] = num[i]/max*100
    sum += num[i]

print(sum/n)