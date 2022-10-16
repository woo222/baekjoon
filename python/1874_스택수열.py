n = int(input())
stack = []
num = []
result = []
item = 1

for i in range(n):
    num.append(int(input()))

for i in range(n):
    # num이 스택에 없으며 있을 때 까지 +(push)
    while (num[i] not in stack):
        if ("NO" in result): break
        stack.append(item)
        result.append('+')
        item += 1

    # num이 stack에 있으면 없어질 때까지 pop
    while (num[i] in stack):
        if(stack.pop() != num[i]):
            result.append('NO')
            break
        else:
            if ("NO" in result): break
            result.append('-')
        
if ("NO" in result):
    print('NO')
else:
    for i in result:
        print(i)
