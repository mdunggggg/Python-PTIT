import re
s = ''
pa = '.!?'
while True:
    try:
        s = input()
        if s[-1] not in pa:
            while len(s) > 0 and s[-1] == ' ':
                s = s[:-1]
            s += '.'
        else:
            while len(s) > 0 and s[-2] == ' ':
                s = s[:-2] + s[-1]
        s = s.strip().lower().split()
        s[0] = s[0][0].upper() + s[0][1:]
        print(' '.join(s))
    except:
        break
