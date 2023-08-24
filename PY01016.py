def process():
    n = input()
    for i in range(0, len(n) , 2):
        for j in range(0, int(n[i + 1]) , 1):
            print(n[i], end= "")
    print()
    return 
for i in range(int(input())):
    process()