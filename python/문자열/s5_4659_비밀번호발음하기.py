# 입력 받기 end일 때 까지
# aeiou 중에 하나라도 포함
def exist_vowel(string, vow):
    exist_res = False
    for s in string:
        for v in vow:
            # 모음이 존재하는지 확인
            # .find의 리턴 값은 인덱스 위치, 여기선 존재하면 0, 그렇지 않으면 -1이다. (한글자이기 때문)
            if((s.find(v))+1): # 해당 알파벳이 모음일 경우
                exist_res = True
            else: # 해당 알파벳이 자음일 경우
                continue
    return exist_res

# aeiou가 3개 이상 중복되거나 자음이 3개 이상 중복 되면 안됨
def overlap3(string, vow):
    over_res = True
    vowel = 0
    novowel = 0
    for s in string:
        if(s in vow):
            novowel = 0
            vowel += 1
        else:
            vowel = 0
            novowel += 1
        if(vowel == 3 or novowel == 3):
            over_res = False
    return over_res

# 같은 글자가 연속으로 2번 오면 안됨.. 단 ee oo 연속은 가능
def continue2(string):
    conti_res = True
    tmp=''
    for i in range(len(string)):
        if(string[i] == tmp):
            conti_res = False
            if(string[i] == 'e' or string[i] == 'o'):
                conti_res = True
        tmp = string[i]
    return conti_res

loop = True
password = []
vowel = "aeiou"
i = 0


while (loop):
    password.append(input())
    if password[i] == 'end':
        loop = False
        password.remove('end')

    i += 1

for psw in password:
    exist_v = exist_vowel(psw, vowel)
    over_v = overlap3(psw, vowel)
    cont_v = continue2(psw)
    if (exist_v and over_v and cont_v):
        print('<%s> is acceptable.' %psw)
    else:
        print('<%s> is not acceptable.' %psw)