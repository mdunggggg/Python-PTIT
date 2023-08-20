import math
def process():
    s = input()
    for i in range(0 , len(s) // 2):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s[len(s) - i - 1]) - ord(s[len(s) - i - 2])):
            print("NO")
            return
    print("YES")   
    return 
for i in range(int(input())):
    process()