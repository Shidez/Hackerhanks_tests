while True:
    n = int(input())
    if n not in range(1, 151):
        continue
    else:
        for i in range(1, n + 1):
            i = str(i)
            print(i, end='')
        break