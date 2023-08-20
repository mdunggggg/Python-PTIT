n = input().lower()
if len(n) >= 3 and n[-3:] == ".py":
    print("yes")
else:
    print("no")