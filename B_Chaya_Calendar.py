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
    n = integer()
    a = lst()
    x = a[0]
    for i in a[1:]:
        p = ceil(x,i)
        if i*p==x:
            p+=1
        x = i*p

        

    print(x)


t = integer()



for _ in range(t):
    
    solve()

