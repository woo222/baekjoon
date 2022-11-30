# 피보나치 수 - 재귀호출
def fib(n):
    if(n == 1 or n == 2):
        return 1
    else:
        global count
        count += 1
        return fib(n-1) + fib(n-2)

# 피보나치 수 - 동적 프로그래밍
def fibonacci(n):
    f = []
    f.append(1)
    f.append(1)
    cnt = 0
    for i in range(2, n):
        cnt += 1
        f.append(f[i-1] + f[i-2])
    return cnt

count = 1
n = int(input())
fib(n)
print(count, fibonacci(n))