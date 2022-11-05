# 스택
from sys import stdin
stack = []
num = int(input())
for i in range(num):
    command = stdin.readline().split()
    com = command[0]
    
    if (com == "push"):
        val = command[1]
        stack.append(val)

    elif (com == "pop"):
        if not stack:
            print(-1)
        else:
            print(stack.pop())

    elif (com == "size"):
        print(len(stack))

    elif (com == "empty"):
        if not stack:
            print(1)
        else:
            print(0)

    elif (com == "top"):
        if not stack:
            print(-1)
        else:
            print (stack[-1])
