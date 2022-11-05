from collections import deque

n, m = map(int, input().split())
number = list(map(int, input().split()))

deq = deque(i for i in range(1, n+1))

count = 0

for i in range(m):
    while True:
        if (deq[0] == number[i]):
            deq.popleft()
            break
        else:
            if(len(deq) / 2 > deq.index(number[i])):
                deq.append(deq.popleft())
                count += 1
            else:
                deq.appendleft(deq.pop())
                count += 1

print(count)