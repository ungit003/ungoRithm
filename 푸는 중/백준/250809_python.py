# 1920

"""
재귀를 리스트 슬라이싱으로 짜면 결국 리스트를 순회해야해서 속도가 느려짐
프린트를 매번 하지말고 숫자 자체만 리턴
def finder(list, number):
    # print(list, number)
    if len(list) <= 3:
        if number in list:
            return print(1)
        else:
            return print(0)
    if len(list) // 2 * 2 == len(list):
        center_index = len(list) // 2 - 1
    else:
        center_index = (len(list) - 1) // 2
    # print(len(list), center_index)
    center_number = list[center_index]
    # print(center_number)
    if center_number == number:
        return print(1)
    elif center_number > number:
        finder(list[ : center_index], number)
    elif center_number < number:
        finder(list[center_index + 1 : ], number)"""

"""def finder(list, number, l_index, r_index):
    if l_index > r_index:
        return 0
    # print(list, number, l_index, r_index)
    center_index = (l_index + r_index) // 2
    # print(center_index)
    center_number = list[center_index]
    # print(center_number)
    if center_number == number:
        return 1
    elif center_number > number:
        return finder(list, number, l_index, center_index - 1)
    elif center_number < number:
        return finder(list, number, center_index + 1, r_index)

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
findings = list(map(int, input().split()))

nums.sort()
# print(nums)
for finding in findings:
    if nums[-1] < finding or nums[0] > finding:
        print(0)
        continue
    print(finder(nums, finding, 0, N - 1))"""

# N = int(input())
# nums = set(map(int, input().split()))
# M = int(input())
# findings = list(map(int, input().split()))

# for target in findings:
#     print(1 if target in nums else 0)

#10815

"""N = int(input())
nums = set(map(int, input().split()))
M = int(input())
findings = list(map(int, input().split()))

for finding in findings:
    print(1 if finding in nums else 0, end=' ')"""

# 1260

from collections import deque

def DFS(start):
    global visited_dfs, dfs_list
    end_points = []
    for edge in edges:
        if edge[0] == start:
            end_points.append(edge[1])
    if end_points:
        for end_point in end_points:
            if visited_dfs[end_point] == False:
                visited_dfs[end_point] = True
                dfs_list.append(end_point)
                DFS(end_point)

def BFS(start):
    global visited_bfs, bfs_list
    end_points = deque([start])
    while end_points:
        end_point = end_points.popleft()
        if visited_bfs[end_point] == False:
            visited_bfs[end_point] = True
            bfs_list.append(end_point)
        for edge in edges:
            if edge[0] == end_point and visited_bfs[edge[1]] == False:
                end_points.append(edge[1])

N, M, V = map(int, input().split())
edges = []
for _ in range(M):
    edge = list(map(int, input().split()))
    edges.append(edge)
    switched_edge = [edge[1], edge[0]]
    edges.append(switched_edge)
edges.sort()

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)
visited_dfs[0] = visited_bfs[0] = True

dfs_list = []
bfs_list = []
dfs_list.append(V)
bfs_list.append(V)
visited_dfs[V] = visited_bfs[V] = True

DFS(V)
BFS(V)
for num in dfs_list:
    print(num, end=' ')
print()
for num in bfs_list:
    print(num, end=' ')