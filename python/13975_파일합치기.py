result = []
T = int(input())

for i in range(T):
    total = 0
    k = int(input())
    page = list(map(int, input().split()))

    for j in range(k-1):
        if(len(page)==1):
            sum = page.pop(0)
        else:
            a = min(page)
            page.remove(a)
            b = min(page)
            page.remove(b)
            sum = a + b
        total += sum
        page.append(sum)

    result.append(total)

for i in result:
    print(i)