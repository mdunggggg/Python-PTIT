for t in range (int(input())):
    p , q = input().split()
    str = input().split()
    if len(str) == 1:
        x = str[0]
        y = input()
    else:
        x = str[0]
        y = str[1]
    num1 = (int)(x.replace(p, q)) + (int)(y.replace(p, q))
    num2 = (int)(x.replace(q, p)) + (int)(y.replace(q, p))
    print(min(num1, num2), max(num1, num2))
