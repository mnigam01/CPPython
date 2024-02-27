import math

def solve():
    x, y = map(int, input().split())
    if x >= y:
        f = 1
        if x & 1 and x != 1:
            f = 1 + (x - 1) ** 2
        elif x % 2 == 0:
            f = x ** 2

        if x & 1:
            print(f + (y - 1))
        else:
            print(f - (y - 1))
    else:
        
        f = 1
        x1 = x
        x = y
        if x & 1 and x != 1:
            f = 1 + (x - 1) ** 2
        elif x % 2 == 0:
            f = x ** 2
        if x & 1:
            print(f + (x - 1) + (x - x1))
        else:
            print(f - (x - 1) - (x - x1))

t = int(input())
for _ in range(t):
    solve()
