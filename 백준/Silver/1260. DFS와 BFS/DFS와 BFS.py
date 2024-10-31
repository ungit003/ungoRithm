def dfs(c):
    visited1.append(c)

    # for elem in adjL[c]:
    #     if elem not in visited1:
    #         dfs(elem)

    for elem in adjL.get(c, []):
        if elem not in visited1:
            dfs(elem)

from collections import deque


def bfs(s, q):
    q.append(s)

    # while q:
    #     node = q.popleft()
    #     if node not in visited2:
    #         visited2.append(node)
    #     for elem in adjL[node]:
    #         if elem not in visited2:
    #             q.append(elem)

    while q:
        node = q.popleft()
        if node not in visited2:
            visited2.append(node)
        for elem in adjL.get(node, []):
            if elem not in visited2:
                q.append(elem)

# def bfs(s, q):
#     visited2.append(s)
#     # print('v', visited2)
#     for elem in adjL[s]:
#         if elem not in visited2 and elem not in q:
#             q.append(elem)
#             # print('q', q)
#     while q:
#         bfs(q.pop(0), q)
#         # print('q2', q)


N, M, V = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

adjL = {}
for edge in edges:
    # if edge[0] in adjL:
    #     adjL[edge[0]].append(edge[1])
    #     print(adjL, 3)
    # if edge[1] in adjL:
    #     adjL[edge[1]].append(edge[0])
    #     print(adjL, 4)
    # if edge[0] not in adjL:
    #     adjL[edge[0]] = [edge[1]]
    #     print(adjL, 1)
    # if edge[1] not in adjL:
    #     adjL[edge[1]] = [edge[0]]
    #     print(adjL, 2)

    if edge[0] not in adjL:
        adjL[edge[0]] = [edge[1]]
        # print(adjL, 1)
    else:
        adjL[edge[0]].append(edge[1])
        # print(adjL, 3)
    if edge[1] not in adjL:
        adjL[edge[1]] = [edge[0]]
        # print(adjL, 2)
    else:
        adjL[edge[1]].append(edge[0])
        # print(adjL, 4)

for key in adjL:
    adjL[key].sort()
# print(adjL)

visited1 = []
dfs(V)
print(*visited1)

visited2 = []
que = deque()
bfs(V, que)
print(*visited2)
