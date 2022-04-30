"""
# 시간초과
def square (i, j, N):
    if((i//N)%3==1 and (j//N)%3==1):
        print(" ", end='')
    else:
        if((N//3)==0):
            print("*", end='')
        else:
            square(i,j,N/3)

n =int(input())
for i in range (0,n):
    for j in range(0,n):
        square(i,j,n)
    print()
"""
n = int(input())
