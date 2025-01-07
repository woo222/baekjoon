from sys import stdin

task = [0] * 31

for _ in range(28):
    student = int(stdin.readline().strip())
    task[student] = 1

for i in range(1, 31):
    if task[i]:
        continue
    print(i)