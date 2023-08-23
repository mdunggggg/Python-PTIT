n = int(input())
list = [float(i) for i in input().split()]
sum = 0
count = 0
Max = max(list)
Min = min(list)
for i in list:
    if i != Max and i != Min:
        sum += i
        count += 1
print("{:.2f}".format(sum / count))