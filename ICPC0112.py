isNotPrime = [0] * 2000000
isNotPrime[0] = 1
isNotPrime[1] = 1
for i in range (2, int(2000000 ** 0.5)):
    if isNotPrime[i] == 0:
        for j in range(i * i, 2000000, i):
            isNotPrime[j] = 1

def process():
    cnt = 0
    for i in range(int(input())-5):
        if isNotPrime[i] == False and isNotPrime[i+6] == False:
            if isNotPrime[i+2] == False or isNotPrime[i+4] == False:
                cnt += 1
    print(cnt)
    return 
for i in range(int(input())):
    process()
   