result = []
T = int(input())

for i in range(T):
    total = 0
    k = int(input())
    page = list(map(int, input().split()))

    for j in range(k-1):
        page.sort()
        if(len(page)==1):
            sum = page.pop(0)
        else:
            sum = page.pop(0) + page.pop(0)
        total += sum
        page.append(sum)

    result.append(total)

for i in result:
    print(i)