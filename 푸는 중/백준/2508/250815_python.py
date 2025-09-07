# 2577

a = int(input())
b = int(input())
c = int(input())
res = str(a * b * c)
for i in range(10):
    ans = 0
    for j in range(len(res)):
        if res[j] == str(i):
            ans += 1
    print(ans)