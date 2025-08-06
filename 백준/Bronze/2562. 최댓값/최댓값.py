num = 0
max_num = 0
for i in range(9):
    think = int(input())
    if think > max_num:
        num = i
        max_num = think
print(max_num)
print(num+1)