cnt = 10
se = set()
while True:
    list = [int(i) % 42 for i in input().split()]
    cnt -= len(list)
    se.update(list)
    if cnt == 0:
        print(len(se))
        break