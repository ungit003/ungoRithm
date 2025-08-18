from collections import deque

def finder(now):
    visited = [0] * 100001
    queue = deque([(now, 0)])

    ans_time = abs(N - K)
    while queue:
        check, time = queue.popleft()
        if check == K:
            ans_time = time
            break
        visited[check] = 1
        if check > 1 and visited[check-1] == 0:
            queue.append((check-1, time+1))
        if check < 99999 and visited[check+1] == 0:
            queue.append((check+1, time+1))
        if check <= 50000 and visited[check*2] == 0:
            queue.append((check*2, time+1))
    return ans_time

N, K = map(int, input().split())
print(finder(N))