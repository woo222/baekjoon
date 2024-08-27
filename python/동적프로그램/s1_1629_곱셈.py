a, b, c = map(int, input().split())

def modular (a, b, c):
    if b == 1:
        return a % c
    else:
        if b%2 == 0:
            return (modular(a,b//2, c) ** 2) % c
        else:
            return ((modular(a,b//2, c)** 2) * a) % c
        
print(modular(a, b, c))