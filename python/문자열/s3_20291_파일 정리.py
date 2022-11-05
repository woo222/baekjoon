n = int(input())
file_list = []
result = {}

for i in range(n):
    filename = input().split('.')[1]

    if(filename not in result):
        result[filename] = 1
    else:
        result[filename] += 1

for key, value in sorted(result.items()):
    print(key, value)