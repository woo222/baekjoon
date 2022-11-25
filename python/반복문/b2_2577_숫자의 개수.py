a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)

lst = [0] * 10
for m in mul:
    lst[int(m)] += 1

for i in range(10):
    print(lst[i])

'''
더 나은 풀이
rst = list(str(a * b * c))
for i in range(10):
    print(rst.count(str(i)))
'''