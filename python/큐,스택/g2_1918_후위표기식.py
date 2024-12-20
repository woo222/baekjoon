from sys import stdin
exp = stdin.readline().strip()

stack = []

for i in exp:
    if i.isalpha():
        print(i, end='')
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and (stack[-1] != '('):
            print(stack.pop(), end='')
        stack.pop()
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(), end='')
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and (stack[-1] != '('):
            print(stack.pop(), end='')
        stack.append(i)
while stack:
    print(stack.pop())