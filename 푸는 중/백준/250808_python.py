# 1181

"""def sorting_func(list):
    return (len(list), list)

N = int(input())
words = set()
for _ in range(N):
    word = input()
    words.add(word)

new_words = sorted(words, key=sorting_func)
for word in new_words:
    print(word)"""

#2751

"""import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
for num in nums:
    print(num) """

# 10814 ~ing

N = int(input())
users = set()
for _ in range(N):
    user = list(input().split())
    # user[0] = int(user[0])
    users.add(user)
print(users)
sorted_users = sorted(list(users))
for user in sorted_users:
    print(user[0], user[1])