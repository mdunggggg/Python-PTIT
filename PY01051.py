def calc(n):
    cur = 0
    for i in range(len(n)):
        cur += int(n[i])
    return cur >= 10 and cur == int(str(cur)[::-1])
for t in range(int(input())):
    n = input()
    if calc(n):
        print("YES")
    else:
        print("NO")



