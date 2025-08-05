def new_cal(a, b):
    return (a + b) * (a - b) 

a, b = map(int, input().split())
print(new_cal(a, b))