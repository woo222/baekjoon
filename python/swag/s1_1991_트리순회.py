import sys
n = int(input())

tree = {}

for i in range(n):
    a, b, c = sys.stdin.readline().split()
    tree[a] = [b, c]

def before(dic, key):
    print(key, end='')
    left, right = dic[key]
    if (left != '.'):
        before(dic, left)
    if (right != '.'):
        before(dic, right)
    else:
        return

def during(dic, key):    
    left, right = dic[key]
    if (left != '.'):
        during(dic, left)
    print(key, end='')
    if (right != '.'):
        during(dic, right)
    else:
        return

def after(dic, key):    
    left, right = dic[key]
    if (left != '.'):
        after(dic, left)
    if (right != '.'):
        after(dic, right)
    print(key, end='')
    return

before(tree, 'A')
print()
during(tree, 'A')
print()
after(tree, 'A')