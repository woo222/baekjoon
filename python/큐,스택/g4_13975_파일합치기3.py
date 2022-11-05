from heapq import heappush, heappop, heapify

result = []
T = int(input())

for i in range(T):
    total = 0
    k = int(input())
    page = list(map(int, input().split()))
    heapify(page)

    for j in range(k-1):
        if(len(page)==1):
            sum = heappop(page)
        else:
            sum = heappop(page)+ heappop(page)
        total += sum
        heappush(page, sum)

    result.append(total)

for i in result:
    print(i)