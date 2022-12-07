n = int(input())

for i in range(n):
    answer = input()
    rst = 0
    bonus = 1
    for a in answer:
        if(a == 'O'):
            rst += bonus
            bonus += 1
        else:
            bonus = 1
    print(rst)