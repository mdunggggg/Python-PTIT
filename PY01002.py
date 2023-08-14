import re
list_number = list(map(int, re.findall(r'\d+', input())))
if(list_number[0] + list_number[1] == list_number[2]):
    print("YES")
else:
    print("NO")