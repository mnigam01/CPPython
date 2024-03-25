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
    tot = sum(a)
    if tot%3==0:
        print(0);return
        gh(0)
        return
    if (tot+1)%3==0:
        print(1);return
        gh(1)
        return
    for i in a:
        if (tot-i)%3==0:
            print(1);return
            gh(1)
            return
    print(2);return
    gh(2)
    return
    


t = 1
t = integer()

for _ in range(t):
    
    solve()

