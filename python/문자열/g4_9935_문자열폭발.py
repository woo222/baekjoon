'''
스택 사용
스택에 문자열 쌓기 -> 폭발마지막 문자와 같으면 스택 pop
'''

from sys import stdin
string_check = stdin.readline().strip()
bomb = stdin.readline().strip()

s_list = []
b_len = len(bomb)

for i in string_check:
    s_list.append(i)

    if bomb == ''.join(s_list[-b_len:]):
        for _ in range(b_len):
            s_list.pop()
    
if not s_list:
    print('FRULA')
else:
    print(''.join(s_list))


# 시간 초과
# from sys import stdin
# string_check = stdin.readline().strip()
# bomb = stdin.readline().strip()

# while(bomb in string_check):
#     string_check = string_check.replace(bomb, '')
    
    
# if not string_check:
#     print('FRULA')
# else:
#     print(string_check)