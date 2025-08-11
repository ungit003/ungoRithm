N = int(input())
orders = []
for _ in range(N):
    orders.append(input().split())
    
stack = []
for i in range(N):
    if orders[i][0] == 'push':
        stack.append(orders[i][1])
    elif orders[i][0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            pop_number = stack.pop()
            print(pop_number)
    elif orders[i][0] == 'size':
        print(len(stack))
    elif orders[i][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif orders[i][0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])