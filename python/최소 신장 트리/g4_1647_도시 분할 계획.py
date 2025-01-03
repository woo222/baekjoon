arr = []

n, m = map(int,input().split())

mspan = [i for i in range(n+1)]
answer = 0
last = 0

def getP(x):
    if (mspan[x] == x): return x
    mspan[x] = getP(mspan[x])
    return mspan[x]

def unionP(x, y):
    x = getP(x)
    y = getP(y)
    if (x < y): mspan[y] = x
    else: mspan[x] = y

def findP(x, y):
    return getP(x) == getP(y)


for i in range(m):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])
arr.sort(key=lambda x:(x[2], x[1]))

for i in range(m):
    if not(findP(arr[i][0], arr[i][1])):
        answer += arr[i][2]
        last = arr[i][2]
        
        unionP(arr[i][0], arr[i][1])

print(answer-last)