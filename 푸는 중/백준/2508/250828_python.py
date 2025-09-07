# 27433

def cal():
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n+1):
            res *= i
        return res
n = int(input())
print(cal())