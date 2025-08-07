def finder(x, y):
    ans = 0
    min_num = 0
    max_num = 0
    if x >= y:
        min_num = y
        max_num = x
    else:
        min_num = x
        max_num = y
    for i in range(1, min_num+1):
        if (max_num % i == 0) and (min_num % i == 0):
            ans = i
    return ans

n, m = map(int, input().split())

print(finder(n, m))
print(n * m // finder(n, m))