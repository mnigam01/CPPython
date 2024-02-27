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
    n,a = integer(),lst()
    b = matrixNum(n-1)
    for i in range(n-1):
        x = a[i]
        cnt = x//b[i][0]
        a[i+1]+=b[i][1]*cnt
    print(a[-1])


t = 1



for _ in range(t):
    
    solve()

