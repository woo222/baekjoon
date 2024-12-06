v, e = map(int, input().split())

arr = []
mspan = [i for i in range(v+1)]
answer = 0

def getP(x):
    if (mspan[x] == x): return x
    mspan[x] = getP(mspan[x])
    return mspan[x]

def unionP(x, y):
    x = getP(x)
    y = getP(y)
    #print('x', x)
    #print('y', y)
    if (x < y): mspan[y] = x
    else: mspan[x] = y

def findP(x, y):
    return getP(x) == getP(y)


for i in range(e):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])
arr.sort(key=lambda x:x[2])

#print(arr)
#print(mspan)

for i in range(e):
    #print('i', i)
    #print('arr[i][0]', arr[i][0])
    #print('arr[i][1]', arr[i][1])
    if not(findP(arr[i][0], arr[i][1])):
        answer += arr[i][2]

        unionP(arr[i][0], arr[i][1])

print(answer)