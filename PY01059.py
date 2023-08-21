def process():
    n = input()
    sum = 0
    product = 1
    flag = 0
    for i in range (0, len(n)):
        if i % 2 == 0:
            sum += int(n[i])
        else:
            if n[i] != '0':
                flag = 1
                product *= int(n[i])

    if flag == 0:
        print(sum, 0)
    else:
        print(sum, product)
    return 
for i in range(int(input())):
    process()