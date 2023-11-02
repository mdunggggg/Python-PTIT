f = open('DATA.in', 'r')
def process():
    n, s = int(f.readline()), f.readline().strip()
    cur = 0
    for i in range(len(s)):
        cur += int(s[i]) * (2 ** (len(s) - i - 1))
    ans = ""
    while cur > 0:
        tmp = cur % n
        cur //= n
        if tmp < 10:
            ans += str(tmp)
        else: 
            ans += chr(tmp - 10 + ord('A'))
    print(ans[::-1])
    return 
for i in range(int(f.readline())):
    process()