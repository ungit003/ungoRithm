def finder(node):
    visited[node] = 1
    for i in range(1, N+1):
        if edges[node][i] == 0:
            continue
        if visited[i] == 1:
            continue
        finder(i)
    return

N = int(input())
M = int(input())
edges = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a][b] = edges[b][a] = 1

visited = [0] * (N+1)
finder(1)
print(sum(visited)-1)