while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if (a*a + b*b == c*c) or (c*c + a*a == b*b) or (b*b + c*c == a*a):
        print('right')
    else:
        print('wrong')