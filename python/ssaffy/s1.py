test = int(input());

for i in range(test):
    n, k = map(int, input().split());
    number = list(map(int, input().split()));
    a = i + 1;

    for j in range(n):
        num = number[k - 1];
        result = True;

        # 수열의 값 비교
        for li in number:
            if (result and num == li):
                result = True;
            else:
                result = False;

        if (result):
            print("#%d %d" %(a,j));
            break;

        # 작업 수행
        number.append(num);
        number.pop(0);

    # 작업 후 다른 경우
    if (not result):
        print("#%d -1" %a);


