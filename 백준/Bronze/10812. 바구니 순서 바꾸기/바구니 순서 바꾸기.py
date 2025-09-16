N, M = map(int, input().split())
basket = [x for x in range(1, N + 1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    changed_basket = basket[:i - 1] + basket[k - 1:j] + basket[i - 1:k - 1] + basket[j:]
    basket = changed_basket
print(*basket)