answer = input()
if(len(answer) == 1):
        answer = '0' + answer
n = answer
new_n = ''
count = 0

while(True):
    
    new_n = str(int(n[0]) + int(n[1]))
    n = n[-1] + new_n[-1]
    count += 1

    if n == answer:
        break

print(count)