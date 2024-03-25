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
    tot = sum(abs(i) for i in a)
    print(tot)
    


t = 1

for _ in range(integer()):
    
    solve()

