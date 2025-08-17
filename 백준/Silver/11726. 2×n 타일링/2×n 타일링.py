def finder(n):
    ans_list = [0] * (n+1)
    # print(ans_list)
    ans_list[1] = 1
    if n > 1:
        ans_list[2] = 2
    if n > 2:
        for i in range(2, n):
            # print(i)
            ans_list[i+1] = ans_list[i] + ans_list[i-1]
            # print(ans_list)
    return ans_list[n]

n = int(input())
ans = finder(n)
print(ans % 10007)