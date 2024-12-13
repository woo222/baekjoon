from functools import cmp_to_key
import re

# 숫자 문자 구분
# 정규식 사용
def separate_word(w):
    sep = re.findall(r'[a-zA-z]|\d+', w)
    return sep

# cmp_to_key 사용
# 음수:왼쪽 작음/ 양수:오른쪽 작음/ 0:같음
def sort_word(w1, w2):
    w1 = separate_word(w1)
    w2 = separate_word(w2)
    for i in range(min(len(w1), len(w2))):
        if w1[i] == w2[i]:
            continue

        # 문자 문자
        if w1[i].isalpha() and w2[i].isalpha():
            if w1[i].lower() == w2[i].lower():
                if w1[i] < w2[i]:
                    return -1
                return 1
            elif w1[i].lower() < w2[i].lower():
                return -1
            else:
                return 1

        # 숫자 숫자
        elif w1[i].isdigit() and w2[i].isdigit():
            if int(w1[i]) == int(w2[i]):
                if len(w1[i]) != len(w2[i]):
                    return len(w1[i]) - len(w2[i])
            else:
                return int(w1[i]) - int(w2[i])

        # 숫자 문자
        if w1[i].isdigit():
            return -1
        else:
            return 1
    
    return len(w1) - len(w2)


n = int(input())
word = []

# 알파벳, 숫자 구분
for _ in range(n):
    word.append(input())
word.sort(key=cmp_to_key(sort_word))

# 출력
for w in word:
    print(w)