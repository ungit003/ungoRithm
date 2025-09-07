# 10814

"""N = int(input())
users = []
for i, _ in enumerate(range(N)):
    age, name = input().split()
    age = int(age)
    users.append((i, age, name))
# print(users)

users.sort(key = lambda x: (x[1], x[0]))

for user in users:
    print(user[1], user[2])"""

# 11650

"""N = int(input())
coors = []
for _ in range(N):
    x, y = map(int, input().split())
    coors.append((x, y))

coors.sort(key = lambda x: (x[0], x[1]))

for x, y in coors:
    print(x, y)"""

# 11723

M = int(input())
orders = []
for _ in range(M):
    order = input().split()
    if len(order) == 2:
        order[1] = int(order[1])
    orders.append(order)
print(orders)

S = set()
