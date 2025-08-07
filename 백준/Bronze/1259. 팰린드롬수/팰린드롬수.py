def reverse(x):
    for i in range(len(x) // 2):
        if x[i] != x[len(x)-1-i]:
            return 'no'
    return 'yes'

while True:
    x = input()
    if int(x) == 0:
        break
    print(reverse(x))