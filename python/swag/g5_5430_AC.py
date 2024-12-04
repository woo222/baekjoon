import sys
from collections import deque

t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    num = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    flag = True
    printFlag = True
    countR = 0

    for q in p:
        # R이면 맨 뒤에 뽑기
        if q == 'R':
            countR += 1
        elif q == 'D':
            if (not num) or (n <= 0):
                print('error')
                printFlag = False
                break
            else:
                if countR % 2 == 0:
                    num.popleft()
                else:
                    num.pop()

    if(printFlag):
        if (countR % 2 == 0):
            print('[' + ','.join(num) + ']')
        else:
            num.reverse()
            print('[' + ','.join(num) + ']')