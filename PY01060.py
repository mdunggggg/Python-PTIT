def process():
    n = input()
    sum = 0
    product = 1
    for i in range (0, len(n)):
        if i % 2 == 1:
            sum += int(n[i])
        else:
            if n[i] != '0':
                product *= int(n[i])

  
    print(product, sum)
    return 
for i in range(int(input())):
    process()