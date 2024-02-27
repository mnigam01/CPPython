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
    s = ''
    n = integer()
    for i in range(n):
        s+='10'
    s+='1'
    print(s)


t = 1



for _ in range(t):
    
    solve()

