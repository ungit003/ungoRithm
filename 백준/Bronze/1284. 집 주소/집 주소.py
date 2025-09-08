while True:
    a = input()
    if a == "0":
        break
    cnt = 0
    for i in range(len(a)):
        if a[i] == "1":
            cnt += 2
        elif a[i] == "0":
            cnt += 4
        else:
            cnt += 3
    print(cnt + 2 + len(a) - 1)