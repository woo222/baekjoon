n = int(input())
m = 1

while(True):
    if((sum(map(int, str(m))) + m) == n):
        print(m)
        break
    if(m > n):
        print(0)
        break
    m += 1