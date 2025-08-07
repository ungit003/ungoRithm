def binomial_coefficient_cal(n, k):
    if n == 0 or k == 0 or n == k:
        return 1
    return binomial_coefficient_cal(n-1, k) + binomial_coefficient_cal(n-1, k-1)

N, K = map(int, input().split())
print(binomial_coefficient_cal(N, K))