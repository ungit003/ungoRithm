# 10828

"""N = int(input())
orders = []
for _ in range(N):
    orders.append(input().split())
# print(orders)

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
            print(stack[-1])"""

# 10845

"""from collections import deque

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
            print(queue[-1])"""

# 10816

"""N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

check_dict = dict()
for check in checks:
    check_dict[check] = 0
# print(check_dict)

for card in cards:
    if card in check_dict:
        check_dict[card] += 1

# 이렇게 하면 출력 과정에서 순서가 바뀔 수 있음
# for value in check_dict.values():
#     print(value, end=' ')
for check in checks:
    print(check_dict[check], end=' ')

# 다른 방법 1
check_dict = dict()
for card in cards:
    check_dict[card] = check_dict.get(card, 0) + 1  # 카드 개수 세기

for check in checks:  # 입력된 순서대로 출력
    print(check_dict.get(check, 0), end=' ')

# 다른 방법 2
from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

card_counts = Counter(cards)  # cards 내 각 숫자별 등장 횟수 계산

# checks 순서대로 card_counts에서 개수를 가져와서 출력
print(' '.join(str(card_counts[num]) if num in card_counts else '0' for num in checks))"""

# 9012

"""def check_VPS(string):
    ans = 'NO'
    if string[0] == ')':
        return print(ans)
    stack = ['(']
    for i in range(1, len(string)):
        if string[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return print(ans)
            elif stack[-1] == '(':
                stack.pop()
            elif stack[-1] == ')':
                stack.append(')')
    if len(stack) == 0:
        ans = 'YES'
    return print(ans)
    
T = int(input())
PS = []
for _ in range(T):
    PS.append(input())

for case in PS:
    check_VPS(case)"""

# 2164

"""from collections import deque

N = int(input())
cards = deque(range(1, N+1))
# print(cards)

while True:
    if len(cards) == 1:
        break
    cards.popleft()
    moving = cards.popleft()
    cards.append(moving)
print(cards[0])"""

# 1018

def check_change(y, x):
    case1, case2 = 0, 0
    for i in range(y, y+8):
        for j in range(x, x+8):
            if i % 2 == 0:
                if rec[i][j] != ans1[j-x]:
                    case1 += 1
                if rec[i][j] != ans2[j-x]:
                    case2 += 1
            else:
                if rec[i][j] != ans2[j-x]:
                    case1 += 1
                if rec[i][j] != ans1[j-x]:
                    case2 += 1
    return min(case1, case2)

M, N = map(int, input().split())
rec = []
for _ in range(M):
    rec.append(input())

ans1, ans2 = '', ''
for i in range(8):
    if i % 2 == 0:
        ans1 += 'W'
        ans2 += 'B'
    else:
        ans1 += 'B'
        ans2 += 'W'

ans_list = []
for i in range(M-7):
    for j in range(N-7):
        ans_list.append(check_change(i, j))
print(min(ans_list))