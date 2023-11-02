n = int(input())
pre, ans = -1, []
while True:
    try: 
        l = len(input().split())
    except:
        break
    if l == 6:
        input()
        if l != pre:
            ans.append(1)
    else:
        ans.append(2)
        for i in range(3):
            input()
    pre = l
print(len(ans))
for i in ans:
    print(i)
    
