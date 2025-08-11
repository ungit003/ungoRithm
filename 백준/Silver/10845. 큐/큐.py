from collections import deque

N = int(input())
orders = []
for _ in range(N):
    orders.append(input().split())

queue = deque()
for i in range(N):
    if orders[i][0] == 'push':
        queue.append(orders[i][1])
    elif orders[i][0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            pop_left = queue.popleft()
            print(pop_left)
    elif orders[i][0] == 'size':
        print(len(queue))
    elif orders[i][0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif orders[i][0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif orders[i][0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])