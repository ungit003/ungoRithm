from collections import deque

N = int(input())
cards = deque(range(1, N+1))
# print(cards)

while True:
    if len(cards) == 1:
        break
    cards.popleft()
    moving = cards.popleft()
    cards.append(moving)
print(cards[0])