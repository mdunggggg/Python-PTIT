def process():
    sum = input()
    if len(sum) < 3:
        print('NO')
        return
    for i in range(1, len(sum) - 1, 1):
        if sum[i] <= sum[i - 1] and sum[i] <= sum[i + 1]:
            print('NO')
            return
    print('YES')
    return  
for i in range(int(input())):
    process()