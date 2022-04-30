# 스택
<<<<<<< HEAD
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
=======
def push(X, s):
    s.append(X)

def pop():
    return

def size():
    return

def empty():
    return

def top():
    return

num = int(input())
stack = []
for i in range(num):
    com = input()
    if ():
        
>>>>>>> 268d15e018d227b724048a2d4d61dc5b170949b5
