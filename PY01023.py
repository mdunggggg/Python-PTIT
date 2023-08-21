def process():
    n = int(input())
    print("1",end = " ")
    for i in range (2, int(n ** 0.5) + 1, 1):
        if n % i == 0:
            count = 0
            while n % i == 0:
                count += 1
                n //= i
            print("* ", i,"^",count, sep = "", end = " ")
    if n > 1:
        print("* ", n,"^",1, sep = "", end = " ")
    print()
    return 
for i in range(int(input())):
    process()