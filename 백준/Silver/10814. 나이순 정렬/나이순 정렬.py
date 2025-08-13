N = int(input())
users = []
for i, _ in enumerate(range(N)):
    age, name = input().split()
    age = int(age)
    users.append((i, age, name))
# print(users)

users.sort(key = lambda x: (x[1], x[0]))

for user in users:
    print(user[1], user[2])