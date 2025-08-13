N, M = map(int, input().split())
users1 = set()
users2 = set()
for _ in range(N):
    users1.add(input())
for _ in range(M):
    users2.add(input())

users3 = sorted(users1.intersection(users2))
print(len(users3))
for user in users3:
    print(user)