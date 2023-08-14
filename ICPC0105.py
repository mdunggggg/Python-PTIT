import re
def calc(s):
    numbers = map(int, re.findall(r'\d+', s))
    return max(numbers)


t = int(input())
while t > 0:
    s = input()
    print(calc(s))
    t -= 1