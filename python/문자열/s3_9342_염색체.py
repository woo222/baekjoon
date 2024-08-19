# 정규표현식
'''
^ 패턴으로 시작
? 패턴이 0~1번
+ 패턴이 한 번 이상
$ 패턴으로 끝
'''
import re
t = int(input())
alpha = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(t):
    text = input()
    if (alpha.match(text) == None):
        print('Good')
    else:
        print('Infected!')