def process():
    n = input()
    sum = 0
    for i in range (0 , len(n) - 1, 1):
        if abs(int(n[i]) - int(n[i + 1])) != 2:
            print("NO")
            return
        sum += int(n[i])
    sum += int(n[-1])
    if sum % 10 == 0:
        print("YES")
    else:
        print("NO")
    return 
for i in range(int(input())):
    process()