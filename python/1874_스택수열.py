n = int(input())
stack = []
result = []
item = 1

for i in range(n):
    num = int(input())

    while (True):
    # num이 스택에 없으며 있을 때 까지 +(push)
        if(item <= num):
            stack.append(item)
            result.append('+')
            item += 1
        elif(stack.pop() != num):
            result.append('NO')
            break
        else:
            result.append('-')
            break
        
if ("NO" in result):
    print('NO')
else:
    for i in result:
        print(i)
