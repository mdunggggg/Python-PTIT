for t in range(int(input())):
    digits = [int (i) for i in input()]
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] >= 5:
            digits[i - 1] += 1
        digits[i] = 0
    print(''.join([str(i) for i in digits]))
        