def process():
    s = input()
    a = s.split(".")
    if len(a) != 4: 
        print("NO")
        return
    for i in a:
        if i.isdigit() == False:
            print("NO")
            return
        if int(i) < 0 or int(i) > 255:
            print("NO")
            return
    print("YES")
    return 
for i in range(int(input())):
    process()