def process():
    s = input()
    ans = 0
    t = ""
    for i in s:
        if i.isdigit() == True:
            ans += int(i)
        else:
            t += i
    print(''.join(sorted(t)) + str(ans))
    return 
for i in range(int(input())):
    process()