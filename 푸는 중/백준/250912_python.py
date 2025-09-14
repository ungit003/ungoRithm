# 29699

# word = "WelcomeToSMUPC"
# n = int(input())
# print(word[(n-1) % len(word)])

# 1927

import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))