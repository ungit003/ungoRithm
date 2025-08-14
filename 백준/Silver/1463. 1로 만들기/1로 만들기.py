def finder(input, cnt):
    global min_cal
    if cnt > min_cal:
        return
    if input == 1:
        min_cal = cnt
        return
    if input % 3 == 0:
        finder(input // 3, cnt+1)
    if input % 2 == 0:
        finder(input // 2, cnt+1)
    finder(input - 1, cnt+1)

N = int(input())
min_cal = N
finder(N, 0)
print(min_cal)