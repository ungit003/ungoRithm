import ast


def maker():
    first = routes['ICN'].pop()
    travel = ['ICN', first]
    for _ in range(len(tickets)-1):
        next = routes[travel[-1]].pop()
        travel.append(next)


tickets = input()
tickets = ast.literal_eval(tickets)
routes = {}
for 출발, 도착 in tickets:
    if 출발 in routes:
        routes[출발].append(도착)
    else:
        routes[출발] = [도착]
print(routes)
for key in routes:
    routes[key].sort(reverse=True)
print(routes)

ans = maker()
print(ans)