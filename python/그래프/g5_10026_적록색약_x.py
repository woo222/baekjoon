n = int(input())
pic = [[] for _ in range(n)]

for i in range(n):
    color = input()
    for c in color:
        if (c == 'R'):
            pic[i].append(0)
        elif (c == 'G'):
            pic[i].append(1)
        else:
            pic[i].append(2)

