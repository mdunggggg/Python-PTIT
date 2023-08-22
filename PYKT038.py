
b = 8
s = input()
cur = 0
for i in range(len(s)):
    cur +=  int(s[i]) * (2 ** (len(s) - i - 1))

ans = ''
while cur > 0:
    temp = cur % b
    
    if(temp < 10):
        ans += str(temp)
    else:
        ans += chr(temp - 10 + ord('A'))
        
    cur //= b
print(ans[::-1])


