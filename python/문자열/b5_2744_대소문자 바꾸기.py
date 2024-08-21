alp = input()

for a in alp:
    if a.isupper():
        print(a.lower(), end='')
    else:
        print(a.upper(),end='')