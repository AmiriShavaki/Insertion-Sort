a = list(map(int, input().split()))

for i in range(1, len(a)):
    flg = False
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            flg = True
            a[j], a[j - 1] = a[j - 1], a[j]
        else:
            break
    if flg:
        print(" ".join(map(str, a)))
