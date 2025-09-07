# 1978

"""def isprime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

N = int(input())
nums = list(map(int, input().split()))

ans = 0
for i in range(N):
    if isprime(nums[i]) == True:
        ans += 1
print(ans)"""

# 2798

"""def blackjack(list, number, sum):
    new_list = sorted(list)
    answer_list = []
    for i in range(number):
        for j in range(i+1, number):
            for k in range(j+1, number):
                if new_list[i] + new_list[j] + new_list[k] <= sum:
                    answer_list.append(new_list[i] + new_list[j] + new_list[k])
    answer_list.sort()
    return answer_list[-1]

N, M = map(int, input().split())
cards = list(map(int, input().split()))

print(blackjack(cards, N, M))"""

# 1259

"""def reverse(x):
    for i in range(len(x) // 2):
        if x[i] != x[len(x)-1-i]:
            return 'no'
    return 'yes'

while True:
    x = input()
    if int(x) == 0:
        break
    print(reverse(x))"""

# 1546

"""N = int(input())
nums = list(map(int, input().split()))

ans = sum(nums) * 100 / max(nums) / N
print(ans)"""

# 2609

"""def finder(x, y):
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
print(n * m // finder(n, m))"""

# 2292

"""0 / 1 - 6 / 7 - 18 / 19 - 36 / 37 - 60 / 61 - 
1, 6, 12, 18, 
n = (1) * 6 - 1 * 6 + 1 -> 1, 
    (1 + 2) * 6 - 2 * 6 + 1 -> 2, 
    (1 + 2 + 3) * 6 - 3 * 6 + 1 -> 3"""

"""N = int(input())

ans = 1
while True:
    size = list(range(1, ans + 1))
    print(ans, size)
    if sum(size) * 6 - ans * 6 + 1 >= N:
        break
    ans += 1

print(ans)"""

# 11050

"""def binomial_coefficient_cal(n, k):
    if n == 0 or k == 0 or n == k:
        return 1
    return binomial_coefficient_cal(n-1, k) + binomial_coefficient_cal(n-1, k-1)

N, K = map(int, input().split())
print(binomial_coefficient_cal(N, K))"""

# 1181 ~ing

def cal_word(list, word_length):
    sorted_list = []

    num = len(list)
    num_list = []
    for i in range(word_length):
        for j in range(num_list):
            num_list.append(len(list[j][i]))
    return sorted_list

def word_sorting(list, word_max_length):
    ans_list = []

    length_list = []
    for i in range(1, word_max_length + 1):
        if list[i][0] == i:
            length_list.append(list[i][1])
        if len(length_list) >= 2:
            cal_word(length_list)
        if len(length_list):
            ans_list.extend(length_list, i)
            length_list.clear()
    return ans_list

N = int(input())
words = []
max_length = 0

for _ in range(N):
    word = input()
    word_len = len(word)
    words.append([word_len, word])
    if max_length < word_len:
        max_length = word_len

words.sort()
for i in range(N):
    print(words[i][1])