def lst():
    return list(map(int, input().strip().split()))


def integer():
    return int(input())

def ceil(x,y):
    return int(-(-x  // y))

def st():
    return input()


def matrixNum(m):
    return [lst() for i in range(m)]

def matrixStr(m):
    return [list(st()) for i in range(m)]

def solve():
    n =integer()
    if n==1:
        print(1);return
    prv = -1
    for i in range(1,33):
        if 2**i<=n:
            prv = 2**i
        else:break
    print(prv)
    


t = 1
t = integer()

for _ in range(t):
    
    solve()

