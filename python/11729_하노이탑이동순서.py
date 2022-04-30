# 하노이 탑 이동 순서
def Hanoi(n, start, temp, to):
    if (n==1):
        print (start, to)
        return

    Hanoi (n-1, start, to, temp)

    print(start, to)

    Hanoi (n-1, temp, start, to)

N = int(input())

print(2**N-1)
Hanoi(N, 1, 2, 3)